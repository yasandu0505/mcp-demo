from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

BASE_URL = "http://localhost:8000"

# Tool: get_document
@app.post("/tool/get_document")
def get_document_tool(payload: dict):
    document_id = payload.get("document_id")

    if not document_id:
        raise HTTPException(status_code=400, detail="document_id required")

    response = requests.post(f"{BASE_URL}/document/{document_id}")
    return response.json()

# Tool: get_related_documents to the document
@app.post("/tool/get_related_documents")
def get_related_documents_tool(payload: dict):
    document_id = payload.get("document_id")

    if not document_id:
        raise HTTPException(status_code=400, detail="document_id required")

    response = requests.post(f"{BASE_URL}/document-rel/{document_id}")
    return response.json()


# Tool: search_documents
@app.post("/tool/search_documents")
def search_documents_tool(payload: dict):
    query = payload.get("query")

    if not query:
        raise HTTPException(status_code=400, detail="query required")

    response = requests.post(f"{BASE_URL}/search", json={"query": query})
    return response.json()


# Tool: dashboard status
@app.post("/tool/get_dashboard_status")
def dashboard_tool():
    response = requests.get(f"{BASE_URL}/dashboard-status")
    return response.json()