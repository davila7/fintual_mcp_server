# File: prompts.py
from mcp.server.fastmcp.prompts import base
from typing import List

class FintualMCPPrompts:
    """Prompts implementation for Fintual MCP server"""
    
    @staticmethod
    def assets_provider_prompt(assets_provider: str) -> List[base.Message]:
        """Prompt to check if a provider is a Fintual asset administrator."""
        return [
            base.UserMessage(f"{assets_provider} es administradora de activos de Fintual?"),
        ]
    
    @staticmethod
    def conceptual_asset_prompt(provider: str) -> List[base.Message]:
        """Prompt to get conceptual assets of a provider."""
        return [
            base.UserMessage(f"Cuáles son los activos conceptuales de la administradora de activos {provider}"),
        ]