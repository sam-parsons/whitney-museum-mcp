import os
import pytest

from src.client import client


pytestmark = pytest.mark.skipif(
    os.getenv("SMOKE") != "1",
    reason="Set SMOKE=1 to run live smoke tests",
)


def test_smoke_artists_live():
    r = client.get("/artists")
    assert r["success"] is True
    assert r["status_code"] == 200
    assert r.get("data") is not None


def test_smoke_artwork_not_found_live():
    r = client.get("/artworks/does-not-exist")
    # Allow either 404 or 400 depending on API behavior
    assert r["success"] is False
    assert r["status_code"] in (404, 400)

