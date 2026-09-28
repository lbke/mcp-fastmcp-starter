
from typing import Literal

from app.server import mcp


@mcp.prompt
def mcp_expert(language: str, framework: Literal["FastMCP", "Skybridge", "mcp-use", "MCP SDK"] = "FastMCP"):
    """
    Defines the role for an MCP expert.
    """
    return f"""You are an expert of model context protocol.
Your favourite language is {language}.
Your favourite MCP framework is {framework}
"""
