"""
Minimal external API client scaffold for the MCP server template.
Hardcodes the base URL to the public API and keeps implementation tiny.
Includes a small stdlib-based HTTP GET.
"""

from typing import Any, Dict, Optional, Union
import json
from urllib import parse as urlparse
from urllib import request as urlrequest
from urllib.error import HTTPError, URLError


class ApiClient:
    """Very small client with a fixed base URL and stdlib HTTP."""

    def __init__(self, base_url: str = "https://whitney.org/api/", default_timeout_seconds: float = 15.0) -> None:
        self.base_url: str = base_url.rstrip("/")
        self.default_timeout_seconds: float = default_timeout_seconds

    def build_url(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> str:
        endpoint_clean = endpoint.lstrip("/")
        base = f"{self.base_url}/{endpoint_clean}"
        if not params:
            return base
        query = urlparse.urlencode(params, doseq=True)
        return f"{base}?{query}"

    def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout_seconds: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Perform a real HTTP GET using urllib, returning parsed JSON when possible."""
        url = self.build_url(endpoint, params)
        req = urlrequest.Request(url)
        req.add_header("Accept", "application/json")
        req.add_header("User-Agent", "mcp-client/0.1")
        if headers:
            for key, value in headers.items():
                req.add_header(key, value)
        timeout = timeout_seconds if timeout_seconds is not None else self.default_timeout_seconds
        try:
            with urlrequest.urlopen(req, timeout=timeout) as resp:
                status_code = resp.getcode()
                raw = resp.read()
                text = raw.decode("utf-8", errors="replace")
                try:
                    data = json.loads(text)
                except json.JSONDecodeError:
                    data = text
                return {
                    "success": True,
                    "status_code": status_code,
                    "url": url,
                    "data": data,
                }
        except HTTPError as e:
            body = e.read().decode("utf-8", errors="replace") if hasattr(e, "read") else ""
            parsed: Union[str, Dict[str, Any]]
            try:
                parsed = json.loads(body) if body else {}
            except json.JSONDecodeError:
                parsed = body or str(e)
            return {
                "success": False,
                "status_code": getattr(e, "code", None),
                "url": url,
                "error": "http_error",
                "message": str(e),
                "data": parsed,
            }
        except URLError as e:
            return {
                "success": False,
                "status_code": None,
                "url": url,
                "error": "network_error",
                "message": getattr(e, "reason", str(e)),
            }

# Create a default client instance
client = ApiClient()

# Export the client
__all__ = ["ApiClient", "client"]
