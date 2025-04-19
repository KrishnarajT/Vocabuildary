import logging
import os
from telegram import Bot
from dotenv import load_dotenv
import csv
import random
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
import asyncio

# Load .env variables
load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load words from CSV
def load_words_from_csv(file_path):
    words = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            words.append(row)
    return words

word_list = load_words_from_csv('words.csv')

# Function to send a random word
async def send_random_word():
    word_entry = random.choice(word_list)
    word = word_entry["word"]
    meaning = word_entry["meaning"]
    example = word_entry["example"]

    message = f"📖 *Word of the Minute*\n\n*{word}*\n\n_{meaning}_\n\nExample: _{example}_"
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='Markdown')
    logger.info(f"Sent word: {word}")

# Main async function
async def main():
    global bot
    bot = Bot(token=TOKEN)
    scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")

    # Add the async job directly
    scheduler.add_job(send_random_word, trigger=IntervalTrigger(minutes=1))
    scheduler.start()

    logger.info("Bot started. Sending a word every minute.")
    
    # Keep the bot running
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())
