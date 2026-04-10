# Ultra-doc-Intelligence-POC



An end-to-end AI-powered document intelligence system that allows users to upload logistics documents (Rate Confirmations, Bills of Lading, Shipment Instructions, Invoices, etc.) and interact with them using natural language.

This project simulates an AI assistant inside a Transportation Management System (TMS) with real-world capabilities like retrieval grounding, guardrails, and confidence scoring.

---

## 🚀 Key Features

### 📄 Document Upload & Processing

* Supports PDF, DOCX, and TXT files
* Parses and extracts text using document loaders
* Intelligent chunking using Recursive Character Text Splitter
* Generates embeddings using transformer models (MiniLM)
* Stores embeddings in a vector database (ChromaDB)

---

### 🔍 Ask Questions (RAG Pipeline)

* Ask natural language questions such as:

  * "What is the carrier rate?"
  * "Who is the consignee?"
  * "When is pickup scheduled?"
* Uses Retrieval-Augmented Generation (RAG)
* Ensures answers are grounded in document context
* Returns:

  * Answer
  * Supporting source chunks
  * Confidence score

---

### 🛑 Guardrails (Hallucination Control)

* Prevents incorrect or hallucinated responses
* Uses:

  * Similarity threshold filtering
  * Context-only answer enforcement
* Returns:

  * `"Not found in document"` when information is missing

---

### 📊 Confidence Scoring

* Provides a confidence score for every answer
* Based on:

  * Retrieval similarity
  * Average relevance of retrieved chunks

**Formula:**

```
confidence = avg(similarity_scores) * 100
```

---

### 📦 Structured Data Extraction

Extracts key shipment details into structured JSON format:

```json
{
  "shipment_id": null,
  "shipper": null,
  "consignee": null,
  "pickup_datetime": null,
  "delivery_datetime": null,
  "equipment_type": null,
  "mode": null,
  "rate": null,
  "currency": null,
  "weight": null,
  "carrier_name": null
}
```

* Uses LLM-based extraction
* Returns `null` for missing fields

---

### 🖥️ Minimal UI (Streamlit)

* Upload logistics documents
* Ask questions interactively
* View:

  * Answers
  * Confidence scores
  * Source context
* Run structured extraction with one click

---

## 🧠 System Architecture

User (Streamlit UI)
↓
FastAPI Backend (API Layer)
↓

**Document Processing Pipeline:**

* Document Loader (PDF/DOCX/TXT)
* Text Chunking
* Embedding Generation
* Vector Storage (ChromaDB)

**Query Pipeline:**

* Query Embedding
* Similarity Search (Top-K Retrieval)
* Guardrail Filtering
* LLM Answer Generation
* Confidence Scoring

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** Streamlit
* **RAG Framework:** LangChain
* **Vector Database:** ChromaDB
* **Embeddings:** HuggingFace (MiniLM)
* **LLM:** OpenAI / compatible LLM
* **Language:** Python

---

## 📦 Installation

```bash
git clone https://github.com/your-username/Ultra-doc-Intelligence-POC.git
cd ultra-doc-ai

python -m venv venv
source venv/Scripts/activate   # Windows Git Bash

pip install -r requirements.txt
```

---

## ▶️ Running the Application

### 🟢 Start Backend (FastAPI)

```bash
python -m uvicorn app:app --reload
```

Runs on:

```
http://127.0.0.1:8000
```

---

### 🟢 Start Frontend (Streamlit)

```bash
streamlit run frontend/app.py
```

Runs on:

```
http://localhost:8501
```

---

## 🔗 API Endpoints

* `POST /upload` → Upload and process document
* `POST /ask` → Ask questions about document
* `POST /extract` → Extract structured shipment data

---

## 🧠 Chunking Strategy

* RecursiveCharacterTextSplitter
* Chunk Size: 800
* Overlap: 150

**Reason:**
Preserves semantic context across logistics fields like rates, addresses, and dates.

---

## 🔍 Retrieval Method

* Embedding-based similarity search
* Top-K retrieval (k=4)
* Distance-based ranking

---

## 🛑 Guardrails Strategy

* Reject answers below similarity threshold
* Force answers strictly from retrieved context
* Fallback response:

```
"Not found in document"
```

---

## 📊 Confidence Scoring Method

* Based on average similarity of retrieved chunks

```
confidence = avg(similarity_scores) * 100
```

---

## ⚠️ Known Limitations

* OCR-heavy PDFs may fail in text extraction
* Multiple shipments in a single document can reduce accuracy
* Ambiguous fields (e.g., multiple dates) may confuse extraction
* No schema validation for extracted data

---

## 🚀 Future Improvements

* Hybrid retrieval (BM25 + vector search)
* Cross-encoder re-ranking
* Multi-document querying
* Highlight answer spans in UI
* LangGraph-based agent workflows
* Voice-based interaction
* Schema validation for structured extraction

---

## 🏆 Key Learnings

* Built a complete RAG-based AI system
* Implemented real-world guardrails for hallucination control
* Designed a confidence scoring mechanism
* Integrated FastAPI backend with Streamlit frontend
* Debugged production-level issues across services

---

## 👩‍💻 Author

**Shravani Jagtap**


---
