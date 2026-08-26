import logging
from fastapi import FastAPI
import inngest
import inngest.fast_api
from inngest.experimental import ai

from dotenv import load_dotenv
import uuid  # to generate unique IDs
import os
import datetime

from data_loader import load_and_chunk_pdf, embed_texts
from vector_db import QdrantStorage
from custom_types import RAGChunkAndSrc, RAGUpsertresult, RAGSearchResult, RAGQueryResult

load_dotenv() # load environment variables from .env file

inngest_client = inngest.Inngest(
    app_id = "rag_app",
    logger = logging.getLogger("uvicorn"),
    is_production = False,
    serializer = inngest.PydanticSerializer() # defines the types of different variable 
)

@inngest_client.create_function(
    fn_id = "RAG: Ingest PDF",
    trigger = inngest.TriggerEvent(event = "rag/ingest_pdf")
)
async def rag_ingest_pdf(ctx: inngest.Context):
    def _load(ctx: inngest.Context) -> RAGChunkAndSrc:
        pdf_path = ctx.event.data["pdf_path"]
        source_id = ctx.event.data.get("source_id", pdf_path)
        chunks = load_and_chunk_pdf(pdf_path)
        return RAGChunkAndSrc(chunks = chunks, source_id = source_id)

    chunks_and_src = await ctx.step.run("load-and-chunk", lambda: _load(ctx), output_type = RAGChunkAndSrc)
    return chunks_and_src.model_dump()

app = FastAPI()


inngest.fast_api.serve(app,inngest_client,[rag_ingest_pdf])
