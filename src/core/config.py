import os
from dotenv import load_dotenv

load_dotenv('env/.env', override=True)

API_TOKEN = os.getenv("API_TOKEN")
SERVER = int(os.getenv("SERVER", 0))
DB_NAME = os.getenv("DB_NAME", 'postgres')
USERNAME = os.getenv("USERNAME", 'postgres')
PASSWORD = os.getenv("PASSWORD", '')
HOST = os.getenv("HOST", 'localhost')
PORT = int(os.getenv("PORT", 5432))
