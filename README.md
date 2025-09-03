## MCP Server for Whitney Museum API

[![CI](https://github.com/sam-parsons/whitney-museum-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/sam-parsons/whitney-museum-mcp/actions/workflows/ci.yml)
[![Docker Hub](https://img.shields.io/docker/pulls/samparsons269/whitney-museum-mcp.svg)](https://hub.docker.com/r/samparsons269/whitney-museum-mcp)
[![Docker Image Size](https://img.shields.io/docker/image-size/samparsons269/whitney-museum-mcp/latest)](https://hub.docker.com/r/samparsons269/whitney-museum-mcp)

Minimal [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that exposes a few read-only tools backed by the Whitney Museum public API.

### References
- API landing and docs: [Whitney API](https://whitney.org/api/), [Whitney API docs](https://whitney.org/about/website/api)
- Open data (CSV) repository: [Open Access GitHub](https://github.com/whitneymuseum/open-access)

## Tools

Registered MCP tools (current set):
- `artists_list` — List artists from the public API
- `artist_get(artist_id)` — Get a single artist by ID
- `artworks_list` — List artworks from the public API
- `artwork_get(artwork_id)` — Get a single artwork by ID
- `exhibitions_list` — List exhibitions from the public API
- `exhibition_get(exhibition_id)` — Get a single exhibition by ID
- `events_list` — List events from the public API
- `event_get(event_id)` — Get a single event by ID


## Install

Requirements: Python 3.12+

```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

Alternatively:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```


## Development

Run tests:
```bash
pytest
```

## License

This project is open source. Please check the license file for details.
