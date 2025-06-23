from fastapi import APIRouter
from db.database import get_latest_messages, get_alerts

router = APIRouter()

@router.get("/latest_messages")
async def latest_messages(limit: int = 20):
    return await get_latest_messages(limit)

@router.get("/alerts")
async def alerts():
    return await get_alerts()
