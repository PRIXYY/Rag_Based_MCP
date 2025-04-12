# MCP Document QA Server

This is an MCP (Modular Command Platform) server built to help you **ingest documents** and **ask questions** about them. Powered by the GroundX API, the server enables seamless document parsing and querying.

## 🧠 Features

- **Ingest Tool**: Upload new documents to the server.
- **Answer Tool**: Ask questions and receive context-aware answers based on the ingested documents.
- Built with **FastMCP**, uses the **GroundX API** for document parsing and intelligence.

## 🚀 Getting Started

### 1. Fork the Repository

Start by forking this repository to your own GitHub account.

### 2. Open in Cursor

Open the forked repository in [Cursor](https://www.cursor.sh/).

### 3. Add MCP Integration

- Use the **"Add MCP"** option in Cursor.
- The platform will automatically detect the included `mcp.json` file.

### 4. Tools Available

Once the MCP server is loaded, you will have access to two tools:

- `ingest_documents`: Ingest new documents to the system.
- `answer_query`: Ask questions and get answers based on the ingested documents.

## 🔧 Configuration

### GroundX API Key

Make sure to **add your GroundX API key** in the `server.py` file:

```python
# server.py
GROUNDX_API_KEY = "your_api_key_here"
