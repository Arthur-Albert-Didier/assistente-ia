from app.brain.ai import perguntar_ia


async def executar_comando(mensagem: str, intencao: str, usuario_id: int) -> str:
    """
    Ponto central de execução de comandos.
    Cada intenção será expandida com sua própria lógica nas próximas fases.
    """

    if intencao == "comando":
        return await _registrar_atividade(mensagem, usuario_id)

    if intencao == "consulta":
        return await _consultar_historico(mensagem, usuario_id)

    if intencao == "lembrete":
        return await _criar_lembrete(mensagem, usuario_id)

    return "Não entendi o comando. Tente de outra forma."


async def _registrar_atividade(mensagem: str, usuario_id: int) -> str:
    # TODO (Fase 2): extrair tipo e duração, salvar no banco
    # Por enquanto, usa a IA para confirmar o registro
    prompt = (
        f"O usuário disse: '{mensagem}'\n"
        "Ele quer registrar uma atividade. Confirme o registro de forma curta e amigável, "
        "mencionando o que foi registrado. Responda em português."
    )
    return await perguntar_ia(prompt)


async def _consultar_historico(mensagem: str, usuario_id: int) -> str:
    # TODO (Fase 2): buscar dados reais do banco de dados
    prompt = (
        f"O usuário perguntou: '{mensagem}'\n"
        "Ainda não há dados salvos no sistema. Informe isso de forma simpática "
        "e diga que o histórico estará disponível em breve. Responda em português."
    )
    return await perguntar_ia(prompt)


async def _criar_lembrete(mensagem: str, usuario_id: int) -> str:
    # TODO (Fase 2): extrair data/hora e salvar lembrete no banco
    prompt = (
        f"O usuário disse: '{mensagem}'\n"
        "Ele quer criar um lembrete. Confirme que o lembrete foi anotado de forma curta e amigável. "
        "Responda em português."
    )
    return await perguntar_ia(prompt)
