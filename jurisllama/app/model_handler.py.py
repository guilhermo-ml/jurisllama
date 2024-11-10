#app/model_handler

from langchain_groq import ChatGroq
from app.config import Config

def initialize_chat_model():
    """Inicializa o modelo Groq."""
    return ChatGroq(api_key=Config.GROQ_API_KEY, model_name=Config.MODEL_NAME, temperature=0)
