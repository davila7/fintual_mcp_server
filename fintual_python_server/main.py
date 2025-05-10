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

# Get Asset provider by ID Tool
@mcp.tool()
def get_asset_provider_by_id(asset_provider_id: int) -> str:
    """Get the asset provider by ID from Fintual API."""
    response_text = ""
    url = f"https://fintual.cl/api/asset_providers/{asset_provider_id}"
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

# Get Conceptual Asset by Asset Provider ID Tool
@mcp.tool()
def get_conceptual_asset_by_asset_provider_id(asset_provider_id: int) -> str:
    """Get the conceptual asset by asset provider ID from Fintual API."""
    response_text = ""
    url = f"https://fintual.cl/api/asset_providers/{asset_provider_id}/conceptual_assets"
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
def assets_provider_prompt(assets_provider: str) -> str:
    return f"{assets_provider} es administradora de activos de Fintual?"