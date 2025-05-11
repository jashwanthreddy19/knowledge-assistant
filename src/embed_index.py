import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from ingest import load_and_chunk

MODEL_NAME = "all-MiniLM-L6-v2"

def build_faiss_index(chunks):
    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(chunks, convert_to_numpy=True)
    faiss.normalize_L2(embeddings)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)
    return model, index

def retrieve(query, model, index, chunks, k=3):
    q_emb = model.encode([query], convert_to_numpy=True)
    faiss.normalize_L2(q_emb)
    D, I = index.search(q_emb, k)
    return [chunks[i] for i in I[0]]

# Pre-build at import time
_chunks = load_and_chunk()
_embedding_model, _faiss_index = build_faiss_index(_chunks)

def get_relevant_chunks(query, k=3):
    return retrieve(query, _embedding_model, _faiss_index, _chunks, k)