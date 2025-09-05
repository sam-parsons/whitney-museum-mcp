## MCP Server for Whitney Museum API

[![CI](https://github.com/sam-parsons/whitney-museum-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/sam-parsons/whitney-museum-mcp/actions/workflows/ci.yml)
[![Docker Hub](https://img.shields.io/docker/pulls/samparsons269/whitney-museum-mcp.svg)](https://hub.docker.com/r/samparsons269/whitney-museum-mcp)
[![Docker Image Size](https://img.shields.io/docker/image-size/samparsons269/whitney-museum-mcp/latest)](https://hub.docker.com/r/samparsons269/whitney-museum-mcp)

Minimal [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that exposes a few read-only tools backed by the Whitney Museum public API.

### References
- API landing and docs: [Whitney API](https://whitney.org/api/), [Whitney API docs](https://whitney.org/about/website/api)
- Open data (CSV) repository: [Open Access GitHub](https://github.com/whitneymuseum/open-access)

## Use with Cursor and Claude (MCP)

This server supports both stdio and HTTP (Server‑Sent Events) transports. For Cursor and Claude Desktop, the simplest setup is HTTP via `url`.

### Quick start (local HTTP)

1) Run the server locally over HTTP:

```bash
python main.py --http --port 8000
```

2) Verify it’s up:

```bash
open http://localhost:8000/health
```

3) Add to your MCP config as an `url` server.

** location is not guaranteed **
- Cursor (macOS): `~/.cursor/mcp.json`
- Claude Desktop (macOS): `~/Library/Application Support/Claude/mcp.json`

Example entry:

```json
{
  "mcpServers": {
    "whitney-api": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

Restart Cursor/Claude and you should see the `whitney-api` server with the tools listed below.

### Remote (Railway or any HTTPS host)

If you deploy this server (Dockerfile included) and get a public URL, point your MCP client at `https://<your-domain>/mcp`:

```json
{
  "mcpServers": {
    "whitney-api": {
      "url": "https://whitney-museum-mcp-production.up.railway.app/mcp"
    }
  }
}
```

### Optional: stdio transport

You can also run via stdio if you prefer a command‑based server:

```bash
python main.py
```

MCP config example:

```json
{
  "mcpServers": {
    "whitney-api-stdio": {
      "command": "python",
      "args": ["main.py"]
    }
  }
}
```

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
- `guides_list` — List guides from the public API
- `guide_get(guide_id)` — Get a single guide by ID
- `pages_list` — List pages from the public API
- `page_get(page_id)` — Get a single page by ID


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

### Docker (HTTP transport)

Use the published image or build locally. The container serves HTTP on port 8000.

Using Docker Hub image:

```bash
docker pull samparsons269/whitney-museum-mcp:latest
docker run --rm -p 8000:8000 samparsons269/whitney-museum-mcp:latest
```

Build locally:

```bash
docker build -t whitney-museum-mcp .
docker run --rm -p 8000:8000 whitney-museum-mcp
```

Verify:

```bash
curl -s http://localhost:8000/health
open http://localhost:8000/docs
```

### Local Python

HTTP (recommended for Cursor/Claude via `url`):

```bash
python main.py --http --port 8000
```

Stdio (for `command/args` config):

```bash
python main.py
```

### Deploy on Railway

This repo is Docker-ready. Create a new Railway service from this repo or Docker image. Ensure port `8000` is exposed, and Railway will set `PORT`; the image already reads it.

Once deployed, configure Cursor/Claude with your service URL:

```json
{
  "mcpServers": {
    "whitney-api": {
      "url": "https://<your-railway-subdomain>.up.railway.app/mcp"
    }
  }
}
```

## Development

Run tests:
```bash
pytest
```

## License

MIT License. See [LICENSE](./LICENSE) for details.
