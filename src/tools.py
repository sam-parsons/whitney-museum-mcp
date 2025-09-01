"""
MCP tools wrapping minimal public API endpoints.
"""

from typing import Dict, Any
from .client import client


def list_artists() -> Dict[str, Any]:
    """List artists from the public API (minimal wrapper)."""
    return client.get("/artists")


def get_artist(artist_id: str) -> Dict[str, Any]:
    """Get a single artist by ID from the public API (minimal wrapper)."""
    return client.get(f"/artists/{artist_id}")


def list_artworks() -> Dict[str, Any]:
    """List artworks from the public API (minimal wrapper)."""
    return client.get("/artworks")


def get_artwork(artwork_id: str) -> Dict[str, Any]:
    """Get a single artwork by ID from the public API (minimal wrapper)."""
    return client.get(f"/artworks/{artwork_id}")
