from sentence_transformers import SentenceTransformer
import numpy as np

# Load model once when app starts
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text: str):
    return model.encode(text)

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )