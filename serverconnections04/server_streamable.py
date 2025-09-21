from starlette.applications import Starlette
from starlette.routing import Mount, Host

#importamos la clase FastMCP del paquete mcp.server.fastmcp
from mcp.server.fastmcp import FastMCP

#creamos servidor con transporte http streamable
mcp = FastMCP(
    name="Streamable HTTP Server_MCP",
    host="0.0.0.0",
    port=8001,
    mount_path="/streamable-http",
)

#adicionamos una herramienta 
@mcp.tool()
# echo_mcp_server_streamable_http.tool()
def add(x: int, y: int) -> int:
    """Suma dos números enteros."""
    return x + y
    # return {"result": x + y}

 #adiciona un recurso de saludo dinamico al recurso
@mcp.resource("greeting://{name}", name="greeting")
# echo_mcp_server_streamable_http.resource("greeting://{name}", name="greeting")
def get_greeting(name: str) -> str:
    """Devuelve un saludo personalizado."""
    return f"Hola, {name}!"

@mcp.resource("SimpleResource://SimpleResource", name="simpleResource")
# echo_mcp_server_streamable_http.resource("SimpleResource://SimpleResource", name="simpleResource")
def get_simple_resource() -> str:
    """Devuelve un mensaje."""
    return f"Hola, este es un recurso basico estatico que retorna este mensaje!"

#@mcp.prompt("¿Cómo te llamas?")

#Run the server
if __name__ == "__main__":
    mcp.run(transport="streamable-http")





