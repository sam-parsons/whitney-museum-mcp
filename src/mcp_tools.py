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
    list_pages,
    get_page,
)


def setup_mcp_tools(mcp):
    """Setup MCP tools for the server"""
    
    @mcp.tool(description="List artists.")
    def artists_list() -> dict:
        """List artists."""
        return list_artists()

    @mcp.tool(description="Get a single artist by ID.")
    def artist_get(artist_id: str) -> dict:
        return get_artist(artist_id)

    @mcp.tool(description="List artworks.")
    def artworks_list() -> dict:
        """List artworks."""
        return list_artworks()

    @mcp.tool(description="Get a single artwork by ID.")
    def artwork_get(artwork_id: str) -> dict:
        return get_artwork(artwork_id)

    @mcp.tool(description="List exhibitions.")
    def exhibitions_list() -> dict:
        """List exhibitions."""
        return list_exhibitions()

    @mcp.tool(description="Get a single exhibition by ID.")
    def exhibition_get(exhibition_id: str) -> dict:
        return get_exhibition(exhibition_id)

    @mcp.tool(description="List events.")
    def events_list() -> dict:
        """List events."""
        return list_events()

    @mcp.tool(description="Get a single event by ID.")
    def event_get(event_id: str) -> dict:
        return get_event(event_id)

    @mcp.tool(description="List guides.")
    def guides_list() -> dict:
        """List guides."""
        return list_guides()

    @mcp.tool(description="Get a single guide by ID.")
    def guide_get(guide_id: str) -> dict:
        return get_guide(guide_id)

    @mcp.tool(description="List pages.")
    def pages_list() -> dict:
        """List pages."""
        return list_pages()

    @mcp.tool(description="Get a single page by ID.")
    def page_get(page_id: str) -> dict:
        return get_page(page_id)
