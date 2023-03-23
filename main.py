import telegram
import requests
import random

# Telegram bot token
TOKEN = "YOUR TOKEN HERE"

# Unsplash API endpoint
UNSPLASH_API = "https://api.unsplash.com/photos/random"

# Unsplash API access key
UNSPLASH_ACCESS_KEY = "YOUR UNLEASH API KEY HERE"

# Create a Telegram bot instance
bot = telegram.Bot(token=TOKEN)

# Function to send a random picture
async def send_random_picture(chat_id):
    # Retrieve a random image URL from the Unsplash API
    headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
    params = {"orientation": "squarish"}
    response = requests.get(UNSPLASH_API, headers=headers, params=params)
    image_url = response.json()["urls"]["regular"]
    # Download the image
    response = requests.get(image_url)
    # Send the image to the chat
    await bot.send_photo(chat_id=chat_id, photo=response.content)

# Handler for the /random_picture command
async def random_picture_handler(update, context):
    chat_id = update.effective_chat.id
    await send_random_picture(chat_id)

# Create an updater and add the command handler
from telegram.ext import *
application = Application.builder().token(TOKEN).build()

    # Commands
application.add_handler(CommandHandler('start', random_picture_handler))

    # Run bot
application.run_polling(1.0)
