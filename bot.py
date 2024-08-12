import os
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Get environment variables
YOUTUBE_API_KEY = os.getenv('AIzaSyAXrWSorub5-DqY0CrTsedMvS3XmUMfEiM')
TELEGRAM_BOT_TOKEN = os.getenv('7321036373:AAGMeFI9LodNWjNaaD1iNjxSLpb9STYRvhs')

def start(update, context):
    update.message.reply_text('Welcome! Send me a YouTube channel ID, and I will tell you the subscriber count.')

def get_subscribers(channel_id):
    url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={YOUTUBE_API_KEY}'
    response = requests.get(url).json()
    if 'items' in response and response['items']:
        subscriber_count = response['items'][0]['statistics']['subscriberCount']
        return subscriber_count
    else:
        return None

def handle_message(update, context):
    channel_id = update.message.text.strip()
    subscriber_count = get_subscribers(channel_id)
    if subscriber_count:
        update.message.reply_text(f'Subscriber count: {subscriber_count}')
    else:
        update.message.reply_text('Invalid channel ID or no data available.')

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
