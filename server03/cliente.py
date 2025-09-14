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
            "parameters": {
                "type": "object",
                "properties": tool.inputSchema["properties"]
                #"required": [],
            },
        },
    }


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
            result = await session.call_tool("add", arguments={"x": 5, "y": 7})

            function = []

            for tool in tools.tools:
                print("tool: ", tool.name)
                print("Tool", tool.inputSchema["properties"])
                function.append(convert_to_llm_tool(tool))
            
            prompt = "suma 2 a 20"

            #resultados
            print("\nRESULTS:")
            print("\nresponse of recurso")
            print(f"RESPONSE FROM greeting://hello: {content} (MIME type: {mime_type})")
            print("\nresponse of tool")
            print(f"RESPONSE FROM add(5, 7): {result}")