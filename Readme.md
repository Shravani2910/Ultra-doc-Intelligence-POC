# 🚚 Ultra Doc-Intelligence (AI for Logistics Documents)

An AI-powered document intelligence system that allows users to upload logistics documents (Rate Confirmations, BOLs, Invoices, etc.) and interact with them using natural language.

This project simulates an AI assistant inside a Transportation Management System (TMS).

---

## 🚀 Features

### 📄 Document Upload & Processing

* Supports PDF, DOCX, TXT
* Parses and chunks documents intelligently
* Generates embeddings using transformer models
* Stores data in a vector database (ChromaDB)

---

### 🔍 Ask Questions (RAG)

* Ask natural language questions like:

  * "What is the carrier rate?"
  * "Who is the consignee?"
  * "Pickup date?"
* Uses Retrieval-Augmented Generation (RAG)
* Returns:

  * Answer
  * Supporting source text
  * Confidence score

---

### 🛑 Guardrails

* Prevents hallucinations using:

  * Similarity threshold filtering
  * Context-only answering
* Returns:

  * “Not found in document” if answer is missing

---

### 📊 Confidence Scoring

* Based on:

  * Retrieval similarity
  * Average chunk relevance
* Output:

  * Confidence % for each answer

---

### 📦 Structured Extraction

Extract structured shipment data:

```json
{
  "shipment_id": "",
  "shipper": "",
  "consignee": "",
  "pickup_datetime": "",
  "delivery_datetime": "",
  "equipment_type": "",
  "mode": "",
  "rate": "",
  "currency": "",
  "weight": "",
  "carrier_name": ""
}
```

* Returns `null` if fields are missing

---

### 🖥️ Minimal UI

* Built with Streamlit
* Features:

  * Upload document
  * Ask questions
  * View answers + confidence + sources
  * Extract structured data

---

## 🧠 Architecture

User → Streamlit UI
  ↓
FastAPI Backend
  ↓

**Document Processing Pipeline:**

* Loader (PDF/DOCX/TXT)
* Chunking (Recursive splitter)
* Embeddings (MiniLM)
* Vector Store (Chroma)

**Query Pipeline:**

* Embed query
* Retrieve top chunks
* Apply guardrails
* Generate answer (LLM)
* Compute confidence score

---

## ⚙️ Tech Stack

* FastAPI (Backend API)
* Streamlit (UI)
* LangChain (RAG pipeline)
* ChromaDB (Vector store)
* HuggingFace Transformers (Embeddings)
* OpenAI / LLM (Answer generation)

---

## 📦 Installation

```bash
git clone <your-repo-link>
cd ultra-doc-ai

python -m venv venv
source venv/Scripts/activate   # Windows Git Bash

pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Start Backend

```bash
python -m uvicorn app:app --reload
```

### Start Frontend

```bash
streamlit run frontend/app.py
```

---

## 🧪 API Endpoints

* **POST /upload** → Upload document
* **POST /ask** → Ask questions
* **POST /extract** → Extract structured data

---

## 🧠 Chunking Strategy

* RecursiveCharacterTextSplitter
* Chunk size: 800
* Overlap: 150

**Why?**
Preserves context across logistics fields like rate, dates, and addresses

---

## 🔍 Retrieval Method

* Similarity search using embeddings
* Top-K retrieval (k=4)
* Distance-based scoring

---

## 🛑 Guardrails Approach

* Reject answers if similarity < threshold
* Force model to answer only from context
* Return fallback:
  `"Not found in document"`

---

## 📊 Confidence Scoring

* Based on average similarity of retrieved chunks

Formula:

```
confidence = avg(similarity_scores) * 100
```

---

## ⚠️ Failure Cases

* OCR-heavy PDFs (text extraction fails)
* Multiple shipments in one document
* Ambiguous fields (multiple dates)
* Missing structured fields

---

## 🚀 Future Improvements

* Hybrid search (BM25 + vector search)
* Re-ranking using cross-encoders
* Multi-document support
* Highlight answer spans in UI
* LangGraph-based agent workflows
* Voice-based query interface

---

## 🏆 Key Learnings

* Built an end-to-end RAG system
* Implemented real-world guardrails
* Designed confidence scoring logic
* Handled production-level debugging

---

## 👩‍💻 Author

Shravani Jagtap
