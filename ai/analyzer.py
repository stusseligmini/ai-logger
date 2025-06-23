from db.database import db
from datetime import datetime

async def analyze_logs():
    messages = await db.messages.find().to_list(100)
    for msg in messages:
        category = "spam" if "buy" in msg["text"].lower() else "normal"
        await db.messages.update_one({"_id": msg["_id"]}, {"$set": {"analysis": {"category": category}}})

async def detect_bots():
    messages = await db.messages.find().to_list(100)
    for msg in messages:
        is_bot = len(msg["text"]) < 10 and msg["text"].isalnum()
        if is_bot:
            await db.messages.update_one({"_id": msg["_id"]}, {"$set": {"bot_suspect": True}})

async def generate_alerts():
    total = await db.messages.count_documents({})
    bots = await db.messages.count_documents({"bot_suspect": True})
    if total and bots / total > 0.3:
        await db.alerts.insert_one({
            "type": "bot_activity",
            "message": f"{round((bots / total) * 100)}% of messages are from suspected bots.",
            "level": "high",
            "timestamp": datetime.utcnow()
        })
