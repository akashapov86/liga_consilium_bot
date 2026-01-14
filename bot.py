import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    text = update.message.text.lower()

    if "лига ии" in text:
        await update.message.reply_text(
            "🏛️ Лига ИИ на связи!\n"
            "Председатель: ChatGPT\n"
            "Эксперты: Gemini, Grok, DeepSeek, Manus\n\n"
            "Задайте вопрос — начнём консилиум 👇"
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
