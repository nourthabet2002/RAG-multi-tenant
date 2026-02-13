# backend/main.py
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from backend.auth import get_current_tenant
from backend.data_loader import load_documents, search_documents

app = FastAPI(title="Multi-Tenant SaaS API")


class QueryRequest(BaseModel):
    question: str


@app.post("/query")
def query_documents(
    request: QueryRequest,
    tenant: str = Depends(get_current_tenant)
):
    # Load documents for this tenant
    documents = load_documents(tenant)
    results = search_documents(documents, request.question)

    if not results:
        return {
            "answer": "Aucune réponse trouvée pour ce client.",
            "sources": []
        }

    # Concatenate first 300 characters of each matching document
    answer = "\n\n".join([doc["content"][:300] for doc in results])

    return {
        "answer": answer,
        "sources": [doc["filename"] for doc in results]
    }
