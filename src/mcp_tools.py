"""
MCP tools setup for the template server.
This module registers the example MCP tool with the FastMCP instance.
"""

from .tools import list_artists, get_artist, list_artworks, get_artwork


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

    @mcp.tool()
    def artworks_list() -> dict:
        """List artworks from the public API."""
        return list_artworks()

    @mcp.tool()
    def artwork_get(artwork_id: str) -> dict:
        """Get a single artwork by ID."""
        return get_artwork(artwork_id)
