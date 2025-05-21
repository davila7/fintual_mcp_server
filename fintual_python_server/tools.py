# File: tools.py
import json
from typing import Dict, Any, List
from mcp.types import TextContent
import urllib.request

class FintualMCPTools:
    """A class containing tools for the Fintual agent."""

    def __init__(self):
        self._base_url = "https://fintual.cl/api/"
        # Fintual funds 
        self._fund_ids = {
            "very_conservative_streep": 15077,
            "conservative_clooney": 188,
            "moderate_pit": 187,
            "risky_norris": 186
        }

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
    
    def login(self, email: str, password: str) -> Dict[str, List[TextContent]]:
        """
        Authenticates a user with Fintual API and returns an access token
        
        Args:
            email: User's email address
            password: User's password
        
        Returns:
            Response containing the access token if successful
        """
        data = {
            "user": {
                "email": email,
                "password": password
            }
        }
        
        try:
            response = self._post_api_data("access_tokens", data)
            return self._format_response(response)
        except Exception as e:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"Authentication failed: {str(e)}"
                    }
                ]
            }

    
    def asset_providers(self) -> Dict[str, List[TextContent]]:
        """Gets the list of asset providers from the API"""
        data = self._fetch_fintual_data("asset_providers")
        return self._format_response(data)
    
    def get_asset_provider_by_id(self, asset_provider_id: int) -> Dict[str, List[TextContent]]:
        """Gets the asset provider by ID from the API"""
        data = self._fetch_fintual_data(f"asset_providers/{asset_provider_id}")
        return self._format_response(data)
    
    def get_conceptual_asset_by_asset_provider_id(self, asset_provider_id: int) -> Dict[str, List[TextContent]]:
        """Gets the conceptual asset by asset provider ID from the API"""
        data = self._fetch_fintual_data(f"asset_providers/{asset_provider_id}/conceptual_assets")
        return self._format_response(data)
    
    def banks(self) -> Dict[str, List[TextContent]]:
        """Gets the list of banks from the API"""
        data = self._fetch_fintual_data("banks")
        return self._format_response(data)
    
    def get_very_conservative_streep(self, to_date: str = None, from_date: str = None) -> Dict[str, List[TextContent]]:
        """
        Obtiene el valor cuota del fondo Very Conservative Streep (ID: 15077)
        
        Args:
            to_date: Fecha hasta la cual obtener datos (formato YYYY-MM-DD)
            from_date: Fecha desde la cual obtener datos (formato YYYY-MM-DD)
        """
        params = []
        if to_date:
            params.append(f"to_date={to_date}")
        if from_date:
            params.append(f"from_date={from_date}")
        
        endpoint = f"real_assets/15077/days"
        if params:
            endpoint += f"?{'&'.join(params)}"
            
        data = self._fetch_fintual_data(endpoint)
        return self._format_response(data)
    
    def get_conservative_clooney(self, to_date: str = None, from_date: str = None) -> Dict[str, List[TextContent]]:
        """
        Obtiene el valor cuota del fondo Conservative Clooney (ID: 188)
        
        Args:
            to_date: Fecha hasta la cual obtener datos (formato YYYY-MM-DD)
            from_date: Fecha desde la cual obtener datos (formato YYYY-MM-DD)
        """
        params = []
        if to_date:
            params.append(f"to_date={to_date}")
        if from_date:
            params.append(f"from_date={from_date}")
        
        endpoint = f"real_assets/188/days"
        if params:
            endpoint += f"?{'&'.join(params)}"
            
        data = self._fetch_fintual_data(endpoint)
        return self._format_response(data)
    
    def get_moderate_pit(self, to_date: str = None, from_date: str = None) -> Dict[str, List[TextContent]]:
        """
        Obtiene el valor cuota del fondo Moderate Pit (ID: 187)
        
        Args:
            to_date: Fecha hasta la cual obtener datos (formato YYYY-MM-DD)
            from_date: Fecha desde la cual obtener datos (formato YYYY-MM-DD)
        """
        params = []
        if to_date:
            params.append(f"to_date={to_date}")
        if from_date:
            params.append(f"from_date={from_date}")
        
        endpoint = f"real_assets/187/days"
        if params:
            endpoint += f"?{'&'.join(params)}"
            
        data = self._fetch_fintual_data(endpoint)
        return self._format_response(data)
    
    def get_risky_norris(self, to_date: str = None, from_date: str = None) -> Dict[str, List[TextContent]]:
        """
        Obtiene el valor cuota del fondo Risky Norris (ID: 186)
        
        Args:
            to_date: Fecha hasta la cual obtener datos (formato YYYY-MM-DD)
            from_date: Fecha desde la cual obtener datos (formato YYYY-MM-DD)
        """
        params = []
        if to_date:
            params.append(f"to_date={to_date}")
        if from_date:
            params.append(f"from_date={from_date}")
        
        endpoint = f"real_assets/186/days"
        if params:
            endpoint += f"?{'&'.join(params)}"
            
        data = self._fetch_fintual_data(endpoint)
        return self._format_response(data)
    
    def get_fund_data(self, fund_id: int, to_date: str = None, from_date: str = None) -> Dict[str, List[TextContent]]:
        """
        Obtiene el valor cuota de cualquier fondo por su ID
        
        Args:
            fund_id: ID del fondo
            to_date: Fecha hasta la cual obtener datos (formato YYYY-MM-DD)
            from_date: Fecha desde la cual obtener datos (formato YYYY-MM-DD)
        """
        params = []
        if to_date:
            params.append(f"to_date={to_date}")
        if from_date:
            params.append(f"from_date={from_date}")
        
        endpoint = f"real_assets/{fund_id}/days"
        if params:
            endpoint += f"?{'&'.join(params)}"
            
        data = self._fetch_fintual_data(endpoint)
        return self._format_response(data)
    
    def get_very_conservative_streep(self, to_date: str = None, from_date: str = None) -> Dict[str, List[TextContent]]:
        """
        Obtiene el valor cuota del fondo Very Conservative Streep
        
        Args:
            to_date: Fecha hasta la cual obtener datos (formato YYYY-MM-DD)
            from_date: Fecha desde la cual obtener datos (formato YYYY-MM-DD)
        """
        return self.get_fund_data(self._fund_ids["very_conservative_streep"], to_date, from_date)
    
    def get_conservative_clooney(self, to_date: str = None, from_date: str = None) -> Dict[str, List[TextContent]]:
        """
        Obtiene el valor cuota del fondo Conservative Clooney
        
        Args:
            to_date: Fecha hasta la cual obtener datos (formato YYYY-MM-DD)
            from_date: Fecha desde la cual obtener datos (formato YYYY-MM-DD)
        """
        return self.get_fund_data(self._fund_ids["conservative_clooney"], to_date, from_date)
    
    def get_moderate_pit(self, to_date: str = None, from_date: str = None) -> Dict[str, List[TextContent]]:
        """
        Obtiene el valor cuota del fondo Moderate Pit
        
        Args:
            to_date: Fecha hasta la cual obtener datos (formato YYYY-MM-DD)
            from_date: Fecha desde la cual obtener datos (formato YYYY-MM-DD)
        """
        return self.get_fund_data(self._fund_ids["moderate_pit"], to_date, from_date)
    
    def get_risky_norris(self, to_date: str = None, from_date: str = None) -> Dict[str, List[TextContent]]:
        """
        Obtiene el valor cuota del fondo Risky Norris
        
        Args:
            to_date: Fecha hasta la cual obtener datos (formato YYYY-MM-DD)
            from_date: Fecha desde la cual obtener datos (formato YYYY-MM-DD)
        """
        return self.get_fund_data(self._fund_ids["risky_norris"], to_date, from_date)