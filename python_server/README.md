# Python Fintual Server


## Features

## How to use
Clone the repository and run the server using the command provided below.

go to python_dani_mcp and run the following command:
```bash
/path_to_your_uv/.local/bin/uv run mcp install main.py
```

## Usage with CodeGPT

### UV
Add this to your `.codegpt/mcp_config.json` file:
```json
{
  "mcpServers": {
    "Fintual MCP": {
      "command": "/path_to_your_uv/.local/bin/uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/path/to/projects/fintual_mcp_server/python_server/main.py"
      ]
    }
  }
}
```

## Usage with Claude Desktop
Add this to your `claude_desktop_config.json` file:
```json
{
  "mcpServers": {
    "Fintual MCP": {
      "command": "/path_to_your_uv/.local/bin/uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/path/to/projects/fintual_mcp_server/python_server/main.py"
      ]
    }
  }
}
```

## Usage with VSCode
Add this to your `.vscode/mcp.json` file:
```json
{
  "mcp": {
    "servers": {
      "Fintual MCP": {
        "command": "/path_to_your_uv/.local/bin/uv",
            "args": [
                    "run",
                    "--with",
                    "mcp[cli]",
                    "mcp",
                    "run",
                    "/path/to/projects/fintual_mcp_server/python_server/main.py"
                ]
            }
        }
    }
}
```