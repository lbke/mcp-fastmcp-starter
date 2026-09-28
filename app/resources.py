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


@mcp.resource("docs://universal_declaration_of_human_rights/{article_number}")
def get_human_rights(article_number: int):
    match article_number:
        case 1:
            return """All human beings are born free and equal in dignity and rights."""
        case 2:
            return """Everyone is entitled to all the rights and freedoms set forth in this Declaration."""
        case _:
            # Raised error will be readable by the host LLM so it can adapt
            # Client visibility can be fine-tuned
            # using ResourceError + mask_error_details=True
            # @see https://gofastmcp.com/servers/resources#error-handling
            raise ValueError(
                "Only supports articles 1 and 2 of the universal declaration of human rights")
