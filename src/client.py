"""
Minimal HTTP client using httpx with timeouts and basic retry/backoff.
Hardcodes the base URL to the Whitney API and keeps implementation small.
"""

from typing import Any, Dict, Optional
import json
from urllib import parse as urlparse
import time
import httpx


class ApiClient:
    """Small client with a fixed base URL and httpx HTTP."""

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
        etag: Optional[str] = None,
        max_retries: int = 2,
    ) -> Dict[str, Any]:
        """HTTP GET with httpx, JSON parsing, and simple retry/backoff for 429/5xx."""
        url = self.build_url(endpoint, params)
        timeout = timeout_seconds if timeout_seconds is not None else self.default_timeout_seconds

        request_headers = {
            "Accept": "application/json",
            "User-Agent": "whitney-mcp/0.1 (+https://github.com/sam-parsons/whitney-museum-mcp)",
        }
        if headers:
            request_headers.update(headers)
        if etag:
            request_headers["If-None-Match"] = etag

        backoff = 0.5
        attempt = 0
        while True:
            attempt += 1
            try:
                with httpx.Client(timeout=timeout, follow_redirects=True) as client:
                    resp = client.get(url, headers=request_headers)
                status = resp.status_code
                text = resp.text
                try:
                    data = resp.json()
                except json.JSONDecodeError:
                    data = text

                # Retry on transient
                if status in (429, 500, 502, 503, 504) and attempt <= max_retries:
                    time.sleep(backoff)
                    backoff *= 2
                    continue

                result: Dict[str, Any] = {
                    "success": 200 <= status < 300,
                    "status_code": status,
                    "url": url,
                    "data": data,
                }
                etag_resp = resp.headers.get("ETag")
                if etag_resp:
                    result["etag"] = etag_resp
                if not result["success"]:
                    result["error"] = "http_error"
                    result["message"] = text if isinstance(data, str) else None
                return result
            except httpx.RequestError as e:
                if attempt <= max_retries:
                    time.sleep(backoff)
                    backoff *= 2
                    continue
                return {
                    "success": False,
                    "status_code": None,
                    "url": url,
                    "error": "network_error",
                    "message": str(e),
                }

# Create a default client instance
client = ApiClient()

# Export the client
__all__ = ["ApiClient", "client"]
