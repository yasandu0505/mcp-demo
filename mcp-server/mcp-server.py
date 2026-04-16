from fastmcp import FastMCP
import httpx

mcp = FastMCP("My Backend MCP Server")

BASE_URL = "http://localhost:8000"

@mcp.tool()
async def get_dashboard_status():
    """Get dashboard status from backend"""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{BASE_URL}/dashboard-status")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}

@mcp.tool()
async def search_documents(query: str, page: int = 1, limit: int = 50):
    """
    Search documents with pagination.

    Use this when the user wants to:
    - search documents
    - find documents by keyword
    - browse results

    Args:
        query: search text
        page: page number (default 1)
        limit: results per page (default 50)
    """

    payload = {
        "query": query,
        "page": page,
        "limit": limit
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{BASE_URL}/search",
                json=payload
            )
            response.raise_for_status()
            return response.json()

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

if __name__ == "__main__":
    mcp.run()