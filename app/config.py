from dotenv import load_dotenv
import os

load_dotenv()

# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# IA
AI_API_KEY = os.getenv("AI_API_KEY")
AI_MODEL   = os.getenv("AI_MODEL", "claude-sonnet-4-6")

# Banco de dados
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///assistente.db")
