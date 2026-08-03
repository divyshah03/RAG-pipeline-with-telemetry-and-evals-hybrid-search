# RAG Pipeline with Telemetry and Evals
An instrumented, evaluation-driven Retrieval-Augmented Generation (RAG) system for document Q&A — built to measure and prove retrieval quality, not just demo it. Every query is logged, every retrieval is scored, and every pipeline change is validated against a ground-truth evaluation harness before it's called an improvement.

## 🚀 Features
- **Document Ingestion**: Upload PDFs, automatically chunked and embedded into a vector store
- **Semantic + Hybrid Retrieval**: Dense vector search combined with BM25 keyword search for improved recall
- **Cross-Encoder Re-Ranking**: Second-pass relevance scoring on retrieved candidates before generation
- **Full Query Telemetry**: Every query logged with retrieved chunks, similarity scores, and context-utilization tracking
- **Automated Evaluation Harness**: 50+ ground-truth Q&A pairs scored via exact-match (factual) and LLM-as-judge (open-ended)
- **Benchmarked Improvements**: Retrieval precision improved by **[X]%** after hybrid search + re-ranking, validated against baseline
- **Interactive UI**: Upload documents and query them directly through a Streamlit interface

## 🛠️ Tech Stack
### Pipeline
- **Python 3.11**
- **LangChain** - RAG orchestration
- **ChromaDB** - Vector store
- **rank_bm25** - Lexical/hybrid retrieval
- **sentence-transformers** - Cross-encoder re-ranking
- **RAGAS** - Evaluation scoring framework
- **OpenAI API** - Embeddings + generation

### Interface & Telemetry
- **Streamlit** - Upload + query UI
- **SQLite** - Query and retrieval logging
- **Pandas** - Eval result aggregation

## 📋 Prerequisites
- Python 3.11+
- OpenAI API key
- pip / virtualenv

## 🔧 Setup Instructions
1. **Clone and install dependencies**
```bash
   git clone https://github.com/divyshah03/RAG-pipeline-with-telemetry-and-evals-hybrid-search.git
   cd RAG-pipeline-with-telemetry-and-evals-hybrid-search
   pip install -r requirements.txt
```
2. **Configure environment**
```bash
   cp .env.example .env
   # Add your OPENAI_API_KEY to .env
```
3. **Run ingestion**
```bash
   python ingest/load_documents.py
```
4. **Launch the app**
```bash
   streamlit run app.py
```
   App will run on `http://localhost:8501`

## 📊 Evaluation Methodology
This project follows an **evaluation-driven development** approach:
1. Instrument the base retrieval pipeline and log every query, retrieved chunk, and similarity score
2. Analyze logs to identify real retrieval failure modes (not hypothetical ones)
3. Build a ground-truth evaluation set of 50+ Q&A pairs specifically targeting those failure modes
4. Score every pipeline version against that eval set — exact-match for factual questions, LLM-as-judge for open-ended ones
5. Upgrade retrieval (hybrid BM25 + cross-encoder re-ranking) and re-run the same eval set to prove improvement

**Results:**
| Metric | Baseline (dense retrieval only) | After hybrid + re-ranking |
|---|---|---|
| Retrieval Precision@5 | [X]% | [X]% |
| Answer Faithfulness | [X]% | [X]% |
| Exact-Match Accuracy | [X]% | [X]% |

## 📁 Project Structure
