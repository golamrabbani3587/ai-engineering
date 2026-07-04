from fastapi import APIRouter
from services.embedding_service import (
    create_embedding,
    cosine_similarity
)

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)

documents = [
    "How to reset my password",
    "Refund policy for orders",
    "How to contact support",
    "Best laptops for gaming",
    "How to track my order"
]

doc_embeddings = []

for doc in documents:
    doc_embeddings.append({
        "text": doc,
        "embedding": create_embedding(doc)
    })


@router.get("/")
def search(query: str):
    query_embedding = create_embedding(query)

    scores = []

    for doc in doc_embeddings:
        score = cosine_similarity(
            query_embedding,
            doc["embedding"]
        )

        scores.append({
            "text": doc["text"],
            "score": float(score)
        })

    scores.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return scores[:3]