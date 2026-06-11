import os
from dotenv import load_dotenv

load_dotenv(override=False)

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_KEY = os.getenv('API_KEY')
DB_PATH = os.getenv('DB_PATH', 'database/movies.db')
DATE_FORMAT = os.getenv('DATE_FORMAT', '%d.%m.%Y')

print(f"DEBUG TOKEN: {BOT_TOKEN[:20] if BOT_TOKEN else 'NONE'}")
