from langchain_community.vectorstores import FAISS

from backend.embeddings.embedding import get_embedding_model


VECTOR_DB = None


def create_vector_store(text_chunks):
    """
    Create a FAISS vector database from text chunks.
    """

    global VECTOR_DB

    embedding_model = get_embedding_model()

    VECTOR_DB = FAISS.from_texts(
        texts=text_chunks,
        embedding=embedding_model
    )

    return VECTOR_DB


def get_vector_store():
    """
    Return the existing vector database.
    """

    return VECTOR_DB


def similarity_search(query, k=4):
    """
    Retrieve the most relevant chunks.
    """

    if VECTOR_DB is None:
        return []

    docs = VECTOR_DB.similarity_search(
        query,
        k=k
    )

    return docs