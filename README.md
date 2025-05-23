# Fintual MCP Servers
This server enables LLMs to interact with Fintual's API.

# API Endpoints
Swagger: https://fintual.cl/api-docs/index.html

# Servers list
- [Python Server](https://github.com/davila7/fintual_mcp_server/tree/main/fintual_python_server)
- [Typescript Server]() (coming soon)

# Python Server Setup instructions
1- Clone this repository
```bash
git clone https://github.com/davila7/fintual_mcp_server.git
```

2- Install [uv](https://github.com/astral-sh/uv)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

# Add the server
Go to the fintual_python_server folder and run the following command:
```bash
cd fintual_python_server
```

Run the following command:
```bash
uv run mcp install server.py
```

or Add this to your .codegpt/mcp_config.json for CodeGPT or /path/to/Claude/claude_desktop_config.json for Claude Desktop:

```json
{
  "mcpServers": {
    "Fintual MCP Server": {
      "command": "/path_to_your_uv/.local/bin/uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "<path to mcp-servers>/fintual_mcp_server/fintual_python_server/server.py"
      ]
    }
  }
}
```

## Important:
- Replace `/path_to_your_uv/.local/bin/uv` with the actual path to your uv executable.
- Replace `<path to mcp-servers>/fintual_mcp_server/fintual_python_server/server.py` with the actual path to the server.py file of the Fintual MCP server.

## Configuration File Location by Tool
The common JSON configuration should be placed in the following file, depending on the tool you are using:

- **Claude Desktop**: `claude_desktop_config.json`
- **Cursor**: `.cursor/mcp.jso`
- **CodeGPT**: `~/.codegpt/mcp_config.json`

# Tool list
- **asset_provider**: Get the list of asset providers.
- **get_asset_provider_by_id**: Get the asset provider by id.
- **get_conceptual_assets**: Get the list of conceptual assets.
- **banks**: Get the list of banks.

# Prompt list
- **assets_provider_prompt**: Prompt to use the assets_provider tool.
- **conceptual_assets_prompt**: Prompt to use the conceptual_assets tool.

## Example questions to use the tools
1. Question Example:
`Zurich es una administradora de activos de Fintual ?`

2. Question Example:
`Cuales son los bancos integrados en Fintual ?`

1. Question Example:
`Cuales son los activos conceptuales de BANCHILE?`

## Add a Prompt to use the tools from the MCP Server
In Claude Desktop, you can add an speific prompt to use the tools.

- Select assets_provider_prompt
  
<img width="360" alt="Screenshot 2025-05-09 at 23 35 53" src="https://github.com/user-attachments/assets/0e5c1ef0-3c1e-4faf-ad0c-700161f108d1" />

- Add the assets_provider

<img width="606" alt="Screenshot 2025-05-09 at 23 41 10" src="https://github.com/user-attachments/assets/2c5f10db-12f1-4f9c-b406-dd7ccf4fbe03" />

## How it works
- The model will use the tools to answer the questions, but first it will ask for confirmation to use the tools.

<img width="564" alt="Screenshot 2025-05-09 at 23 43 17" src="https://github.com/user-attachments/assets/6f70cb33-1228-490b-906a-8883007daff5" />

- Then the model will read the API response and answer the question.

<img width="574" alt="Screenshot 2025-05-09 at 23 43 53" src="https://github.com/user-attachments/assets/81e2a98e-d90c-44d0-a865-622c33138fe9" />

# What's next
- Add more tools to the MCP Server.
- Add more prompts to use the tools.
- Add typescript support to the MCP Server.
