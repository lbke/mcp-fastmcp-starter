## Prérequis

```
uv tool install fastmcp-slim
```

## Installation

```
git clone https://github.com/lbke/mcp-fastmcp-starter.git mcp-fastmcp-new-app --origin upstream

uv sync
```

## Lancement en mode développement

```
fastmcp run server.py --transport http --reload
```

L'inspector fournit par FastMCP peut ne pas être à jour, il vaut mieux le lancer à côté : 

```
npx @modelcontextprotocol/inspector@latest
```