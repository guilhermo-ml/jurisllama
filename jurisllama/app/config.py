# app/config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do arquivo .env

LLAMA_PARSE_API_KEY = os.getenv("LLAMA_PARSE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
