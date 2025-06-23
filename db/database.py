import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Last inn .env-variabler
load_dotenv()

# Hent URI fra miljøvariabel
uri = os.getenv("MONGODB_URI")

client = MongoClient(uri)
db = client["mydatabase"]
