import pytest
from unittest.mock import Mock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.client import ApiClient, client
from src.tools import list_artists, get_artist, list_artworks, get_artwork, list_exhibitions, get_exhibition, list_events, get_event, list_guides, get_guide, list_pages, get_page


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

    def test_get_artist_empty_raises(self):
        with pytest.raises(ValueError):
            get_artist("")

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

    def test_get_artwork_empty_raises(self):
        with pytest.raises(ValueError):
            get_artwork("")

    def test_list_exhibitions_calls_client(self, monkeypatch):
        seen = {}
        def fake_get(endpoint, params=None, headers=None, timeout_seconds=None):
            seen["endpoint"] = endpoint
            return {"success": True, "data": []}
        monkeypatch.setattr(client, "get", fake_get)

        result = list_exhibitions()
        assert result["success"] is True
        assert seen["endpoint"] == "/exhibitions"

    def test_get_exhibition_calls_client(self, monkeypatch):
        seen = {}
        def fake_get(endpoint, params=None, headers=None, timeout_seconds=None):
            seen["endpoint"] = endpoint
            return {"success": True, "data": {"id": "e1"}}
        monkeypatch.setattr(client, "get", fake_get)

        result = get_exhibition("e1")
        assert result["success"] is True
        assert seen["endpoint"] == "/exhibitions/e1"

    def test_get_exhibition_empty_raises(self):
        with pytest.raises(ValueError):
            get_exhibition("")

    def test_list_events_calls_client(self, monkeypatch):
        seen = {}
        def fake_get(endpoint, params=None, headers=None, timeout_seconds=None):
            seen["endpoint"] = endpoint
            return {"success": True, "data": []}
        monkeypatch.setattr(client, "get", fake_get)

        result = list_events()
        assert result["success"] is True
        assert seen["endpoint"] == "/events"

    def test_get_event_calls_client(self, monkeypatch):
        seen = {}
        def fake_get(endpoint, params=None, headers=None, timeout_seconds=None):
            seen["endpoint"] = endpoint
            return {"success": True, "data": {"id": "ev7"}}
        monkeypatch.setattr(client, "get", fake_get)

        result = get_event("ev7")
        assert result["success"] is True
        assert seen["endpoint"] == "/events/ev7"

    def test_get_event_empty_raises(self):
        with pytest.raises(ValueError):
            get_event("")

    def test_list_guides_calls_client(self, monkeypatch):
        seen = {}
        def fake_get(endpoint, params=None, headers=None, timeout_seconds=None):
            seen["endpoint"] = endpoint
            return {"success": True, "data": []}
        monkeypatch.setattr(client, "get", fake_get)

        result = list_guides()
        assert result["success"] is True
        assert seen["endpoint"] == "/guides"

    def test_get_guide_calls_client(self, monkeypatch):
        seen = {}
        def fake_get(endpoint, params=None, headers=None, timeout_seconds=None):
            seen["endpoint"] = endpoint
            return {"success": True, "data": {"id": "g1"}}
        monkeypatch.setattr(client, "get", fake_get)

        result = get_guide("g1")
        assert result["success"] is True
        assert seen["endpoint"] == "/guides/g1"

    def test_get_guide_empty_raises(self):
        with pytest.raises(ValueError):
            get_guide("")

    def test_list_pages_calls_client(self, monkeypatch):
        seen = {}
        def fake_get(endpoint, params=None, headers=None, timeout_seconds=None):
            seen["endpoint"] = endpoint
            return {"success": True, "data": []}
        monkeypatch.setattr(client, "get", fake_get)

        result = list_pages()
        assert result["success"] is True
        assert seen["endpoint"] == "/pages"

    def test_get_page_calls_client(self, monkeypatch):
        seen = {}
        def fake_get(endpoint, params=None, headers=None, timeout_seconds=None):
            seen["endpoint"] = endpoint
            return {"success": True, "data": {"id": "p1"}}
        monkeypatch.setattr(client, "get", fake_get)

        result = get_page("p1")
        assert result["success"] is True
        assert seen["endpoint"] == "/pages/p1"

    def test_get_page_empty_raises(self):
        with pytest.raises(ValueError):
            get_page("")


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
        # Expect 12 registrations: artists(2), artworks(2), exhibitions(2), events(2), guides(2), pages(2)
        assert mock_mcp.tool.call_count == 12


