"""
Minimal external API client scaffold for the MCP server template.
Hardcodes the base URL to the public API and keeps implementation tiny.
"""

from typing import Any, Dict, Optional


class ApiClient:
    """Very small client with a fixed base URL."""

    def __init__(self, base_url: str = "https://whitney.org/api/") -> None:
        self.base_url: str = base_url.rstrip("/")

    def build_url(self, endpoint: str) -> str:
        endpoint_clean = endpoint.lstrip("/")
        return f"{self.base_url}/{endpoint_clean}"

    def make_request(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Placeholder. Replace with real HTTP logic later."""
        url = self.build_url(endpoint)
        return {
            "success": True,
            "url": url,
            "params": params or {},
            "note": "Placeholder implementation. Add real HTTP calls later.",
        }


# Create a default client instance
client = ApiClient()

# Export the client
__all__ = ["ApiClient", "client"]
