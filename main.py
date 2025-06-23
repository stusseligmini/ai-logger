
from flask import Flask, jsonify, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from db.database import db
from datetime import datetime
import random

app = Flask(__name__)

collection = db["id_logg"]

# 🤖 Dummy AI-funksjon: filtrerer ut duplikater og spam-id-er
def dummy_ai_filter(new_data):
    existing_ids = {doc["id"] for doc in collection.find({}, {"id": 1})}
    filtered = []
    for item in new_data:
        if item["id"] not in existing_ids and "spam" not in item["navn"].lower():
            filtered.append(item)
    return filtered

# 🔁 Scraper-funksjon (dummy for nå)
def run_scraper():
    print("🔄 Kjører scraper...")
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    fake_data = [
        {"id": random.randint(100000, 999999), "navn": f"Bruker_{i}", "gruppe": "TestGruppe", "tid": now}
        for i in range(3)
    ]
    cleaned = dummy_ai_filter(fake_data)
    if cleaned:
        collection.insert_many(cleaned)
        print(f"✅ Logget {len(cleaned)} nye ID-er")
    else:
        print("⚠️ Ingen nye ID-er å logge")

# ⏱️ Start scheduler for scraping hvert 5. minutt
scheduler = BackgroundScheduler()
scheduler.add_job(run_scraper, 'interval', minutes=5)
scheduler.start()

# 🌍 API-endepunkt for frontend
@app.route("/api/logs")
def get_logs():
    logs = list(collection.find({}, {"_id": 0}))
    return jsonify(logs)

# 🖼️ Dashboard (HTML)
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

# 🔁 Kjør Flask (Render bruker miljøvariabel PORT)
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
