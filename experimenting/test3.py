import logging
import os
from telegram import Bot
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import sqlite3
import asyncio
import random

# Load .env variables
load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
DB_FILE = 'vocab.db'

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get a random unsent word
def get_random_unsent_word():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT id, word, meaning, example FROM words WHERE sent = 0')
    rows = c.fetchall()
    if not rows:
        logger.info("All words sent. Resetting.")
        c.execute('UPDATE words SET sent = 0')
        conn.commit()
        c.execute('SELECT id, word, meaning, example FROM words WHERE sent = 0')
        rows = c.fetchall()

    word_entry = random.choice(rows)
    conn.close()
    return word_entry

# Mark a word as sent
def mark_word_sent(word_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('UPDATE words SET sent = 1 WHERE id = ?', (word_id,))
    conn.commit()
    conn.close()

# Function to send a random word
async def send_random_word():
    word_entry = get_random_unsent_word()
    word_id, word, meaning, example = word_entry

    message = f"📖 *Word of the Day*\n\n*{word}*\n\n_{meaning}_\n\nExample: _{example}_"
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='Markdown')
    logger.info(f"Sent word: {word}")

    mark_word_sent(word_id)

# Main async function
async def main():
    global bot
    bot = Bot(token=TOKEN)
    scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")

    # Schedule daily at 9:00 AM
    scheduler.add_job(send_random_word, trigger=CronTrigger(hour=2, minute=55))
    scheduler.start()

    logger.info("Bot started. Will send a word every day at 9:00 AM.")

    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())
