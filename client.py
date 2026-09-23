import asyncio
from fastmcp import Client

# Official example server from MCP protocol
# requires , auth="oauth"
EXAMPLE_CLIENT = "https://example-server.modelcontextprotocol.io/mcp"
# Localhost
LOCAL_CLIENT = "http://localhost:8000/mcp"

# HTTP server
CLIENT_URL = LOCAL_CLIENT

client = Client(CLIENT_URL)


async def main():
    async with client:
        # List available operations
        tools = await client.list_tools()
        resources = await client.list_resources()
        print(resources)
        prompts = await client.list_prompts()

        # Execute operations
        result = await client.call_tool("echo", {"s": "foobar"})
        print(result)


asyncio.run(main())
