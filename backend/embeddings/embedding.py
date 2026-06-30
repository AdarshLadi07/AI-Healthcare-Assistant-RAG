from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config.config import GEMINI_API_KEY

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=GEMINI_API_KEY
)

def get_embedding_model():
    return embeddings