# Support Operations MCP

A local Model Context Protocol (MCP) server that exposes fictional support operations tools to MCP-compatible AI clients.

## Features

- Retrieves fictional incident details by incident ID
- Retrieves fictional service status information
- Retrieves fictional API error and authentication runbooks
- Returns structured JSON responses
- Tested interactively with MCP Inspector

## Available tools

### `get_incident`

Returns details for a fictional support incident.

Example input:

```text
INC-1001
```

### `get_service_status`

Returns the fictional operational status of a service.

Example input:

```text
Orders API
```

### `get_runbook`

Returns a fictional operational runbook.

Available topics:

```text
api-errors
authentication
```

## Run locally

Install the dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Start MCP Inspector:

```powershell
.\.venv\Scripts\mcp.exe dev server.py
```

Open the local link shown in the terminal, connect the server, then open the **Tools** tab to test each tool.

## Project structure

```text
support-operations-mcp/
├── .gitignore
├── README.md
├── requirements.txt
└── server.py
```

## Tech stack

- Python
- Model Context Protocol (MCP)
- MCP Python SDK
- MCP Inspector
- Node.js
- uv

## Note

All incidents, services, statuses, and runbooks in this repository are fictional. No customer or employer data is used.