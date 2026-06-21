import os
from dotenv import load_dotenv

load_dotenv()

# configuring JWT variables
JWT_SECRET = os.getenv("JWT_SECRET")

# configuring DB variables
DB_BASE_URL = os.getenv("DB_DASH_BASE_URL")
DB_WRITE_AUTH_KEY = os.getenv("DB_WRITE_AUTH_KEY")
DB_READ_AUTH_KEY = os.getenv("DB_READ_AUTH_KEY")
DATABASE_ID = os.getenv("DATABASE_ID")
AUTH_TABLE_ID = os.getenv("AUTH_TABLE_ID")
