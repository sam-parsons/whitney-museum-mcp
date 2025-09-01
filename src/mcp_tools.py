"""
MCP tools setup for the template server.
This module registers the example MCP tool with the FastMCP instance.
"""

from .tools import list_artists, get_artist


def setup_mcp_tools(mcp):
    """Setup MCP tools for the server"""
    
    @mcp.tool()
    def artists_list() -> dict:
        """List artists from the public API."""
        return list_artists()

    @mcp.tool()
    def artist_get(artist_id: str) -> dict:
        """Get a single artist by ID."""
        return get_artist(artist_id)
