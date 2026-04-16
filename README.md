# MCP Demo

> Exploring MCP (Model Context Protocol) servers and how to build them.

This project contains a simple example connecting a backend server to an LLM using the MCP protocol.

---

## Prerequisites

- [Claude Desktop](https://claude.com/download) installed on your machine
- Python 3.x

---

## Setup

### 1. Connect the MCP Server to Claude Desktop

Open the Claude Desktop config file:

**macOS:**
```bash
open ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

Add the following configuration:

```json
{
  "mcpServers": {
    "my-backend": {
      "command": "path/to/your/python/env (or just 'python')",
      "args": ["absolute/path/to/mcp-server.py"]
    }
  }
}
```

### 2. Run the Backend Server

```bash
cd server
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## Example Queries

Once Claude Desktop is open and connected, try asking:

- *"List the document types"*
- *"What are the document types available in the system?"*
- *"How many documents do we have?"*
- *"Search me this document number: 2153-12"*