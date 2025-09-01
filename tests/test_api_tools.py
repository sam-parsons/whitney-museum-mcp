import pytest
from unittest.mock import Mock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.client import ApiClient, client
from src.tools import list_artists, get_artist, list_artworks, get_artwork


class TestClient:
    
    def test_build_url_no_params(self):
        c = ApiClient()
        assert c.build_url("/artists") == "https://whitney.org/api/artists"

    def test_build_url_with_params(self):
        c = ApiClient()
        url = c.build_url("/artists", {"page": 2, "q": "a b"})
        assert url.startswith("https://whitney.org/api/artists?")
        assert "page=2" in url
        assert "q=a+b" in url


class TestTools:
    
    def test_list_artists_calls_client(self, monkeypatch):
        calls = {}
        def fake_get(endpoint, params=None, headers=None, timeout_seconds=None):
            calls["endpoint"] = endpoint
            calls["params"] = params
            return {"success": True, "data": []}
        monkeypatch.setattr(client, "get", fake_get)

        result = list_artists()
        assert result["success"] is True
        assert calls["endpoint"] == "/artists"

    def test_get_artist_calls_client(self, monkeypatch):
        captured = {}
        def fake_get(endpoint, params=None, headers=None, timeout_seconds=None):
            captured["endpoint"] = endpoint
            return {"success": True, "data": {"id": "123"}}
        monkeypatch.setattr(client, "get", fake_get)

        result = get_artist("123")
        assert result["success"] is True
        assert captured["endpoint"] == "/artists/123"

    def test_list_artworks_calls_client(self, monkeypatch):
        seen = {}
        def fake_get(endpoint, params=None, headers=None, timeout_seconds=None):
            seen["endpoint"] = endpoint
            return {"success": True, "data": []}
        monkeypatch.setattr(client, "get", fake_get)

        result = list_artworks()
        assert result["success"] is True
        assert seen["endpoint"] == "/artworks"

    def test_get_artwork_calls_client(self, monkeypatch):
        seen = {}
        def fake_get(endpoint, params=None, headers=None, timeout_seconds=None):
            seen["endpoint"] = endpoint
            return {"success": True, "data": {"id": "9"}}
        monkeypatch.setattr(client, "get", fake_get)

        result = get_artwork("9")
        assert result["success"] is True
        assert seen["endpoint"] == "/artworks/9"


class TestMCPRegistration:
    
    def test_setup_registers_tools(self):
        from src.mcp_tools import setup_mcp_tools
        mock_mcp = Mock()
        # mcp.tool() is a decorator factory; simulate by returning identity decorator
        def tool_decorator_factory(*args, **kwargs):
            def decorator(fn):
                return fn
            return decorator
        mock_mcp.tool = Mock(side_effect=tool_decorator_factory)

        setup_mcp_tools(mock_mcp)
        # Expect 4 tool registrations: artists_list, artist_get, artworks_list, artwork_get
        assert mock_mcp.tool.call_count == 4


