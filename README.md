# MCP Build Chess Server

This project is a simple MCP server that retrieves the profile and stats of a chess player.

## Running the Server

Install this MCP server by adding the following JSON code your  JSON config file:

```json
{
    "mcpServers":{
 "chess": {
        "command": "uvx",
        "args": [
          "--from",
          "git+https://github.com/lhamini/mcp-chess.com-api.git",
          "chess"
        ]
      }
    }
}
```