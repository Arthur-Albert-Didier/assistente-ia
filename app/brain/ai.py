import httpx
from app.config import AI_API_KEY

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.1-8b-instant"

SYSTEM_PROMPT = """Você é um assistente pessoal inteligente e direto.
Ajuda o usuário a organizar estudos, registrar hábitos e gerenciar tarefas.
Responda sempre em português, de forma clara e objetiva.
Seja amigável mas sem exageros."""


async def perguntar_ia(mensagem: str) -> str:
    headers = {
        "Authorization": f"Bearer {AI_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": mensagem},
        ],
        "max_tokens": 1024,
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                GROQ_URL,
                headers=headers,
                json=payload,
                timeout=30,
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]

    except httpx.HTTPStatusError as e:
        print(f"Erro na API: {e}")
        return "Tive um problema ao me conectar com a IA. Tente novamente."

    except Exception as e:
        print(f"Erro inesperado: {e}")
        return "Ocorreu um erro inesperado. Tente novamente."