"""
MCP tools setup for the template server.
This module registers the example MCP tool with the FastMCP instance.
"""

from .tools import (
    list_artists,
    get_artist,
    list_artworks,
    get_artwork,
    list_exhibitions,
    get_exhibition,
    list_events,
    get_event,
    list_guides,
    get_guide,
)


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

    @mcp.tool()
    def exhibitions_list() -> dict:
        """List exhibitions from the public API."""
        return list_exhibitions()

    @mcp.tool()
    def exhibition_get(exhibition_id: str) -> dict:
        """Get a single exhibition by ID."""
        return get_exhibition(exhibition_id)

    @mcp.tool()
    def events_list() -> dict:
        """List events from the public API."""
        return list_events()

    @mcp.tool()
    def event_get(event_id: str) -> dict:
        """Get a single event by ID."""
        return get_event(event_id)

    @mcp.tool()
    def guides_list() -> dict:
        """List guides from the public API."""
        return list_guides()

    @mcp.tool()
    def guide_get(guide_id: str) -> dict:
        """Get a single guide by ID."""
        return get_guide(guide_id)
