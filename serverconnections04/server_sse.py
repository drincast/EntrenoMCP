from starlette.applications import Starlette
from starlette.routing import Mount, Host

#importamos la clase FastMCP del paquete mcp.server.fastmcp
from mcp.server.fastmcp import FastMCP

#creamos el servidor para usar sse
mcp = FastMCP(
    name="SSE Server_MCP",
    # host="0.0.0.0",
    port=8000,
)

#creamos servidor con transporte sse
app = Starlette(
    routes=[
        Mount("/sse", app=mcp.sse_app(), name="sse"),        
    ]
)

#adicionamos una herramienta 
@mcp.tool()
def add(x: int, y: int) -> int:
    """Suma dos números enteros."""
    return x + y

 #adiciona un recurso de saludo dinamico al recurso
@mcp.resource("greeting://{name}", name="greeting")
def get_greeting(name: str) -> str:
    """Devuelve un saludo personalizado."""
    return f"Hola, {name}!"

@mcp.resource("SimpleResource://SimpleResource", name="simpleResource")
def get_simple_resource() -> str:
    """Devuelve un mensaje."""
    return f"Hola, este es un recurso basico estatico que retorna este mensaje!"

