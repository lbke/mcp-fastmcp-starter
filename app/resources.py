from app.server import mcp
from fastmcp.resources import HttpResource


mcp.add_resource(
    HttpResource(
        # as seen from client
        # can be obfuscated too
        uri="https://www.lbke.fr/formations/ia/mcp",
        # fetched from server
        url="https://www.lbke.fr/formations/ia/mcp",
        name="Formation MCP LBKE",
        mime_type="text/html",
    )
)
