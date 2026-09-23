from server import mcp


@mcp.tool
def echo(s: str) -> str:
    """Echo the provided string"""
    return s
