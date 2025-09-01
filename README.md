## MCP Server for Whiteney Museum API

[![CI](https://github.com/sam-parsons/whitney-museum-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/sam-parsons/whitney-museum-mcp/actions/workflows/ci.yml)
[![Docker Hub](https://img.shields.io/docker/pulls/samparsons269/whitney-museum-mcp.svg)](https://hub.docker.com/r/samparsons269/whitney-museum-mcp)
[![Docker Image Size](https://img.shields.io/docker/image-size/samparsons269/whitney-museum-mcp/latest)](https://hub.docker.com/r/samparsons269/whitney-museum-mcp)

Minimal [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that exposes a few read-only tools backed by the Whitney Museum public API.

Focus is on core functionality and a clean starting point; additional endpoints and features can be added incrementally.

### References
- API landing and docs: [Whitney API](https://whitney.org/api/), [Whitney API docs](https://whitney.org/about/website/api)
- Open data (CSV) repository: [Open Access GitHub](https://github.com/whitneymuseum/open-access)

## Tools

Registered MCP tools (minimal set):
- `artists_list` — List artists from the public API
- `artist_get(artist_id)` — Get a single artist by ID
- `artworks_list` — List artworks from the public API
- `artwork_get(artwork_id)` — Get a single artwork by ID

These tools are thin wrappers around `GET https://whitney.org/api/*` and return parsed JSON.

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

## Run

HTTP transport (easy to inspect):
```bash
python main.py --http --port 8000
```

Then open:
- `http://localhost:8000/docs` — simple info page
- `http://localhost:8000/tools` — lists registered tools

Stdio transport (for MCP-aware clients):
```bash
python main.py
```

## Usage examples

List tools (HTTP):
```bash
curl http://localhost:8000/tools | jq
```

Call tools via MCP clients (e.g., Cursor) by configuring this server as an MCP provider and invoking tools by name:
- `artists_list`
- `artist_get` with parameter `artist_id`
- `artworks_list`
- `artwork_get` with parameter `artwork_id`

Note: The `/mcp` HTTP endpoint implements the MCP protocol; use through MCP-compatible clients.

## Development

Run tests:
```bash
pytest
```

Code lives in:
- `src/client.py` — minimal HTTP client (urllib)
- `src/tools.py` — tool wrappers
- `src/mcp_tools.py` — registration with FastMCP
- `main.py` — server startup (stdio or HTTP)

## License

This project is open source. Please check the license file for details.
