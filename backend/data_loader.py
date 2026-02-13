import os

# Get absolute path of current file (data_loader.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build safe path to tenants folder
BASE_PATH = os.path.join(BASE_DIR, "tenants")


def load_documents(tenant: str):
    tenant_path = os.path.join(BASE_PATH, tenant)

    # Safety check: ensure tenant folder exists
    if not os.path.exists(tenant_path):
        raise FileNotFoundError(f"Tenant folder not found: {tenant}")

    documents = []

    for filename in os.listdir(tenant_path):
        file_path = os.path.join(tenant_path, filename)

        # Only read text files (optional but professional)
        if os.path.isfile(file_path) and filename.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                documents.append({
                    "filename": filename,
                    "content": content
                })

    return documents


def search_documents(documents, query: str):
    results = []

    for doc in documents:
        if query.lower() in doc["content"].lower():
            results.append(doc)

    return results
