from telethon.sync import TelegramClient
from db.database import save_message
from ai.analyzer import analyze_logs, detect_bots, generate_alerts
import asyncio
import os
import logging

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
group = os.getenv("TELEGRAM_GROUP_URL")

async def start_scraper():
    if not all([api_id, api_hash, group]):
        logging.error("Missing Telegram API credentials. Please set TELEGRAM_API_ID, TELEGRAM_API_HASH, and TELEGRAM_GROUP_URL")
        return
    
    try:
        client = TelegramClient("anon", api_id, api_hash)
        await client.start()
        
        async for message in client.iter_messages(group, limit=20):
            if message.text:
                data = {
                    "message_id": message.id,
                    "text": message.text,
                    "user_id": message.sender_id,
                    "timestamp": str(message.date)
                }
                await save_message(data)
        
        await analyze_logs()
        await detect_bots()
        await generate_alerts()
        
    except Exception as e:
        logging.error(f"Error in telegram scraper: {e}")
    finally:
        await client.disconnect()
