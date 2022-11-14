import os
from dotenv import load_dotenv

load_dotenv("./env/.env")
API_TOKEN = os.getenv("API_TOKEN")
SERVER = int(os.getenv("SERVER", 0))
DB_NAME = os.getenv("DB_NAME", 'postgres')
USER = os.getenv("USER", 'postgres')
PASSWORD = os.getenv("PASSWORD", '')
HOST = os.getenv("HOST", 'localhost')
PORT = int(os.getenv("PORT", 5432))
