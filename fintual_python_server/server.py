# File: server.py
from mcp.server.fastmcp import FastMCP
import tools
import prompts

class FintualMCPServer:
    """ Main class for the Fintual MCP Server. """
    def __init__(self, name: str = "Fintual Python Server"):
        self.name = name
        self.mcp = FastMCP(name)
        self.tools = tools.FintualMCPTools()
        self.prompts = prompts.FintualMCPPrompts()
        self._register_tools()
        self._register_prompts()

    def _register_tools(self) -> None:
        """ Register all tools with the MCP server. """
        self.mcp.tool()(self.tools.asset_providers)
        self.mcp.tool()(self.tools.get_asset_provider_by_id)
        self.mcp.tool()(self.tools.get_conceptual_asset_by_asset_provider_id)
        self.mcp.tool()(self.tools.banks)

    def _register_prompts(self) -> None:
        """ Register all prompts with the MCP server. """
        self.mcp.prompt()(self.prompts.assets_provider_prompt)
        self.mcp.prompt()(self.prompts.conceptual_asset_prompt)

    def run(self, transport: str = "stdio") -> None:
        """Runs the MCP server with the specified transport"""
        self.mcp.run(transport=transport)

# Create a server instance at the module level
server = FintualMCPServer()

# Main entry point
if __name__ == "__main__":
    server.run()