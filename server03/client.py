from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
import json
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

 #crear el cliente
server_params = StdioServerParameters(
    command="mcp",
    args=["run", "server.py"],  #comando para ejecutar el servidor
    env=None, #variables de entorno
)

def convert_to_llm_tool(tool):
    tool_schema = {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description or "",
            "type": "function",
            "parameters": {
                "type": "object",
                "properties": tool.inputSchema["properties"]
                #"required": [],
            },
        },
    }

    print('tool_schema: -->', tool_schema)
    return tool_schema

def call_llm(prompt, functions):
    #usando .env para cargar la clave de API
    from dotenv import load_dotenv
    import os
    print(load_dotenv() )
    token = os.getenv("API_KEY_GHCOP")
    endpoint = os.getenv("ENDPOINT_GHCOP")

    model_name = "gpt-4o"

    print("Calling llm")
    print(token, endpoint)

    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token),
    )

    response = client.complete(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model_name,
        tools = functions,
        temperature=1.,
        max_tokens=1000,
        top_p=1.
    )

    response_message = response.choices[0].message

    functions_to_call = []

    if response_message.tool_calls:
        for tool_call in response_message.tool_calls:
            print("TOOL: ", tool_call)
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)
            functions_to_call.append({"name": name, "args": args})

    return functions_to_call



async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            await session.initialize()

            #listar los recursos disponibles
            #los recursos dinamicos no se listan normalmente, investigar por que
            resources = await session.list_resources()
            print("\nAVAILABLE RESOURCES:")
            for resource in resources.resources:
                print(f"recurso - {resource}")

            #listar las herramientas disponibles
            tools = await session.list_tools()
            print("\nAVAILABLE TOOLS:")
            for tool in tools.tools:
                print(f"herramienta - {tool.name}")

            #Leer un recurso
            # greeting = await session.read_resource("greeting://hello") 
            content, mime_type = await session.read_resource("greeting://EVA")

            #leer herramienta
            result1 = await session.call_tool("add", arguments={"x": 5, "y": 7})

            functions = []

            for tool in tools.tools:
                print("tool llm: ", tool.name)
                print("Tool llm", tool.inputSchema["properties"])
                functions.append(convert_to_llm_tool(tool))
            
            prompt = "por favor suma 3 a 20"

            print()
            functions_to_call = call_llm(prompt, functions)
            print("functions_to_call: ", functions_to_call)

            for f in functions_to_call:
                result2 = await session.call_tool(f["name"], arguments=f["args"])
                print("TOOLS result: ", result2.content)
                # print("TOOLS result: ", result2.content)

            #resultados
            print("\nRESULTS:")
            print("\nresponse of recurso")
            print(f"RESPONSE FROM greeting://hello: {content} (MIME type: {mime_type})")
            print("\nresponse of tool")
            print(f"RESPONSE FROM add(5, 7): {result1}")
            print(f"RESPONSE FROM add of the prompt='{prompt}: {result2}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())