import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI, UploadFile
import shutil
from utils.loader import load_document
from utils.chunker import chunk_docs
from utils.embeddings import get_embeddings
from utils.vectorstore import create_vector_store

app = FastAPI()

vector_db = None

@app.post("/upload")
async def upload(file: UploadFile):
    try:
        path = f"temp/{file.filename}"

        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print("File saved")

        docs = load_document(path)
        print("Docs loaded")

        chunks = chunk_docs(docs)
        print("Chunks created")

        embedding = get_embeddings()
        print("Embeddings ready")

        global vector_db
        vector_db = create_vector_store(chunks, embedding)
        print("Vector DB created")

        return {"message": "Document processed"}

    except Exception as e:
        return {"error": str(e)}

@app.post("/ask")
def ask(query: str):
    docs = retrieve_docs(vector_db, query)

    valid, msg = apply_guardrails(docs)

    if not valid:
        return {
            "answer": msg,
            "confidence": 0
        }

    answer = generate_answer(query, docs)
    confidence = compute_confidence(docs)

    return {
        "answer": answer,
        "confidence": confidence,
        "sources": [d[0].page_content for d in docs]
    }

@app.post("/extract")
def extract():
    docs = vector_db.similarity_search("", k=10)
    data = extract_shipment(generate_answer, docs)

    return data