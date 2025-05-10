# server.py
import urllib.request
import json
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

# Create the MCP server instance
mcp = FastMCP("Fintual MCP Server")

# Asset Providers Tool
@mcp.tool()
def asset_providers() -> str:
    """Get the list of asset providers from Fintual API."""
    response_text = ""
    url = "https://fintual.cl/api/asset_providers"
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; FintualPythonServer/1.0)"
    }
    request = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            response_text = json.dumps(json.loads(response.read()), indent=4)
        else:
            response_text = f"Error: Unable to fetch data, HTTP Code: {response.getcode()}"
    except urllib.error.HTTPError as e:
        response_text = f"Error: {e}"
    return {
        "content": [{
            "type": "text",
            "text": response_text
        }]
    }

# Banks Tool
@mcp.tool()
def banks() -> str:
    """Get the list of banks from Fintual API."""
    response_text = ""
    url = "https://fintual.cl/api/banks"
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; FintualPythonServer/1.0)"
    }
    request = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            response_text = json.dumps(json.loads(response.read()), indent=4)
        else:
            response_text = f"Error: Unable to fetch data, HTTP Code: {response.getcode()}"
    except urllib.error.HTTPError as e:
        response_text = f"Error: {e}"
    return {
        "content": [{
            "type": "text",
            "text": response_text
        }]
    }


# Prompts
@mcp.prompt()
def review_code(assets_provider: str) -> str:
    return f"{assets_provider} es administradora de activos de Fintual?"