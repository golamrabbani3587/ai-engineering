from fastapi import APIRouter
from services.embedding_service import (
    create_embedding,
    cosine_similarity
)


from services.vector_service import (
    search_documents
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
    return search_documents(query)

# router.get("/vector")
# def search(query:str):
#     return search_documents(str)