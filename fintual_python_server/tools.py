# File: tools.py
import json
from typing import Dict, Any, List
from mcp.types import TextContent
import urllib.request
import urllib.parse

class FintualMCPTools:
    """A class containing tools for the Fintual agent."""

    def __init__(self):
        self._base_url = "https://fintual.cl/api/"

    def _fetch_fintual_data(self, endpoint: str) -> Dict[str, Any]:
        """Helper function to fetch data from a given Fintual API endpoint."""
        response_text = ""
        url = f"{self._base_url}/{endpoint}"
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
        except Exception as e:
            response_text = f"An unexpected error occurred: {e}"

        return {
            "content": [{
                "type": "text",
                "text": response_text
            }]
        }

    def _post_api_data(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Helper method to post data to the API (POST requests)"""
        try:
            data_encoded = json.dumps(data).encode('utf-8')
            req = urllib.request.Request(
                f"{self._base_url}/{endpoint}",
                data=data_encoded,
                headers = {
                    "User-Agent": "Mozilla/5.0 (compatible; FintualPythonServer/1.0)"
                },
                method='POST'
            )
            with urllib.request.urlopen(req) as response:
                if response.getcode() == 200:
                    return json.loads(response.read())
                else:
                    raise Exception(f"Error: Response code {response.getcode()}")
        except Exception as e:
            raise Exception(f"Error posting data to API: {str(e)}")

    def _format_response(self, data: Dict[str, Any]) -> Dict[str, List[TextContent]]:
        """Formats data for MCP response"""
        return {
            "content": [
                TextContent(
                    type="text",
                    text=json.dumps(data, indent=4)
                )
            ]
        }
    
    def asset_providers(self) -> Dict[str, List[TextContent]]:
        """Gets the list of asset providers from the API"""
        data = self._fetch_api_data("asset_providers")
        return self._format_response(data)
    
    def get_asset_provider_by_id(self, asset_provider_id: int) -> Dict[str, List[TextContent]]:
        """Gets the asset provider by ID from the API"""
        data = self._fetch_api_data(f"asset_providers/{asset_provider_id}")
        return self._format_response(data)
    
    def get_conceptual_asset_by_asset_provider_id(self, asset_provider_id: int) -> Dict[str, List[TextContent]]:
        """Gets the conceptual asset by asset provider ID from the API"""
        data = self._fetch_api_data(f"asset_providers/{asset_provider_id}/conceptual_assets")
        return self._format_response(data)
    
    def banks(self) -> Dict[str, List[TextContent]]:
        """Gets the list of banks from the API"""
        data = self._fetch_api_data("banks")
        return self._format_response(data)