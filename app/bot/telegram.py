from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from app.config import TELEGRAM_TOKEN
from app.brain.intent import processar_mensagem


async def comando_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! Sou seu assistente pessoal. Como posso te ajudar?"
    )


async def comando_ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "Aqui estão algumas coisas que você pode me pedir:\n\n"
        "• Registre uma corrida de 20 minutos\n"
        "• Estudei Python por 1 hora\n"
        "• Quais tarefas estão pendentes?\n"
        "• Me lembre de revisar matemática amanhã\n"
        "• Quanto estudei esta semana?\n"
    )
    await update.message.reply_text(texto)


async def receber_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = update.message.text
    usuario_id = update.message.from_user.id

    print(f"[{usuario_id}] {mensagem}")

    resposta = await processar_mensagem(mensagem, usuario_id)
    await update.message.reply_text(resposta)


def iniciar_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", comando_start))
    app.add_handler(CommandHandler("ajuda", comando_ajuda))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receber_mensagem))

    print("Bot rodando. Pressione Ctrl+C para parar.")
    app.run_polling()
