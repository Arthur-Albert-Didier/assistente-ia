from app.brain.ai import perguntar_ia
from app.brain.commands import executar_comando


# Palavras-chave que indicam um comando de registro
PALAVRAS_REGISTRO = ["registre", "registra", "anota", "salva", "fiz", "estudei", "corri", "treinei"]

# Palavras-chave que indicam uma consulta
PALAVRAS_CONSULTA = ["quanto", "quantas", "quantos", "quais", "mostre", "me diga", "histórico", "resumo"]

# Palavras-chave que indicam um lembrete
PALAVRAS_LEMBRETE = ["lembre", "lembrete", "me avise", "me lembra"]


def identificar_intencao(mensagem: str) -> str:
    texto = mensagem.lower()

    if any(p in texto for p in PALAVRAS_REGISTRO):
        return "comando"

    if any(p in texto for p in PALAVRAS_CONSULTA):
        return "consulta"

    if any(p in texto for p in PALAVRAS_LEMBRETE):
        return "lembrete"

    return "conversa"


async def processar_mensagem(mensagem: str, usuario_id: int) -> str:
    intencao = identificar_intencao(mensagem)

    print(f"Intenção identificada: {intencao}")

    if intencao in ("comando", "consulta", "lembrete"):
        return await executar_comando(mensagem, intencao, usuario_id)

    # Se for conversa livre, manda para a IA
    return await perguntar_ia(mensagem)
