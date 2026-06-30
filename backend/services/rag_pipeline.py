from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.vector_db.faiss_db import (
    create_vector_store,
    similarity_search,
)

from backend.llm.langchain_gemini import get_llm


def build_vector_database(report_text):
    """
    Build FAISS vector database from report.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(report_text)

    create_vector_store(chunks)

    return len(chunks)


def ask_question(question):

    docs = similarity_search(question)

    if not docs:
        return "Please upload a medical report first."

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    llm = get_llm()

    prompt = f"""
You are an AI Healthcare Assistant.

Answer ONLY from the medical report.

If the answer is not available, say:
"I couldn't find that information in the uploaded report."

Medical Report:

{context}

Question:

{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content