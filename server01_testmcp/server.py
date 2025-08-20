#importamos la clase FastMCP del paquete mcp.server.fastmcp
from mcp.server.fastmcp import FastMCP

#creamos el servidor
mcp = FastMCP("Demo")

#adicionamos una herramienta 
@mcp.tool()
def add(x: int, y: int) -> int:
    """Suma dos números enteros."""
    return x + y

 #adiciona un recurso de saludo dinamico al recurso
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Devuelve un saludo personalizado."""
    return f"Hola, {name}!"





