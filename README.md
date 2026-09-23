## Prerequisites

```
uv tool install fastmcp-slim
```

## Installation

```
git clone https://github.com/lbke/mcp-fastmcp-starter.git mcp-fastmcp-new-app --origin upstream

uv sync
```

## Development mode

```
fastmcp run main.py --transport http --reload
```

FastMCP built-in inspector may not be up-to-date, you can launch it in a separate terminal : 

```
npx @modelcontextprotocol/inspector@latest
```

## Test client

You can run a simple test with `client.py`

```sh
uv run client.py
```

## Structure

We add a separate "main.py" that runs the app, and a "server.py" that can be imported in other files to allow splitting resources, tools etc. into different files.