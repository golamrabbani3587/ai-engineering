import faiss
import numpy as np

from services.embedding_service import (
    create_embedding
)

documents = [
    "How to reset my password",
    "Refund policy for orders",
    "How to contact support",
    "Best laptops for gaming",
    "How to track my order"
]

embeddings = np.array(
    [create_embedding(doc) for doc in documents]
).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)




def search_documents(
    query: str,
    k: int = 3
):
    query_embedding = np.array(
        [create_embedding(query)]
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        k
    )

    return [
        documents[i]
        for i in indices[0]
    ]