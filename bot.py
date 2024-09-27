import logging
import os

from dotenv import load_dotenv
from telegram.ext import (ApplicationBuilder, CommandHandler, MessageHandler,
                          filters)

from ml.model import QuestionAnsweringModel

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables.")

qa_model = QuestionAnsweringModel()


async def start(update, context):
    user = update.effective_user
    logger.info(f"User {user.first_name} started the bot.")
    await update.message.reply_text(
        "Hello! I'm Ken Jennings, ask me anything from Jeopardy!"
    )


async def handle_message(update, context):
    question = update.message.text
    user = update.effective_user

    logger.info(f"Received question from {user.first_name}: {question}")

    try:
        question_number, certainty, answer = qa_model.infer_answer(question)
        logger.info(
            f"Answered question {question_number} with {certainty}% certainty: {answer}"
        )

        await update.message.reply_text(
            f"I know this question, its number is {question_number}. \n"
            f"I'm {certainty}% sure of this. The answer is: {answer}"
        )
    except Exception as e:
        logger.error(f"Error handling question: {str(e)}")
        await update.message.reply_text("Sorry, I couldn't process your question.")


def main():
    logger.info("Starting the Jeopardy QA Bot...")

    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Bot is polling for messages...")
    app.run_polling()


if __name__ == "__main__":
    main()
