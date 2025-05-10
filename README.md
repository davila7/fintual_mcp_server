# Fintual MCP Servers
This repository contains the source code for the Fintual MCP

# API Endpoints
This MCP Server allows you to interact with Fintual's API:
Swagger: https://fintual.cl/api-docs/index.html

# Servers list
- [Python Server](https://github.com/davila7/fintual_mcp_server/tree/main/python_server)
- [Typescript Server]() (coming soon)

# Setup instructions
1- Clone this repository
```bash
git clone https://github.com/davila7/fintual_mcp_server.git
```

2- Install dependencies
Install uv
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Use with Claude Desktop
To use this with Claude Desktop, add the following to your claude_desktop_config.json:
### UV
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
        "<path to mcp-servers>/fintual_mcp_server/python_server/main.py"
      ]
    }
  }
}
```

# Tool list
- **asset_provider**: Get the asset provider of a given asset.
- **banks**: Get the list of banks.

## Example questions to use the tools
`Zurich es una administradora de activos de Fintual ?`

## Add from the MCP Server
In Claude Desktop, you can add an speific prompt to use the tools.

- Select assets_provider_prompt
  
<img width="360" alt="Screenshot 2025-05-09 at 23 35 53" src="https://github.com/user-attachments/assets/0e5c1ef0-3c1e-4faf-ad0c-700161f108d1" />

- Add the provider

<img width="606" alt="Screenshot 2025-05-09 at 23 41 10" src="https://github.com/user-attachments/assets/2c5f10db-12f1-4f9c-b406-dd7ccf4fbe03" />

## How it works
- The model will use the tools to answer the questions, but first it will ask for confirmation to use the tools.

<img width="564" alt="Screenshot 2025-05-09 at 23 43 17" src="https://github.com/user-attachments/assets/6f70cb33-1228-490b-906a-8883007daff5" />

- Then the model will read the API response and answer the question.

<img width="574" alt="Screenshot 2025-05-09 at 23 43 53" src="https://github.com/user-attachments/assets/81e2a98e-d90c-44d0-a865-622c33138fe9" />
