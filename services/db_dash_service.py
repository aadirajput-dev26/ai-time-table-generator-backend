# Central API Layer of DB Dash to call for every service
from config import settings
import requests

BASE_URL = f"{settings.DB_BASE_URL}/{settings.DATABASE_ID}"

WRITE_HEADERS = {
    "Content-Type" : "application/json",
    "auth-key" : settings.DB_WRITE_AUTH_KEY
}

READ_HEADERS = {
    "Content-Type" : "application/json",
    "auth-key" : settings.DB_READ_AUTH_KEY
}

def create_record(table_id: str, payload: dict) -> dict:
    url = f"{BASE_URL}/{table_id}"
    response = requests.post(url, headers=WRITE_HEADERS, json={"records" : [payload]})
    return response.json()


def get_record(table_id: str, filters: str) -> dict:
    url = f"{BASE_URL}/{table_id}?filter={filters}"
    response = requests.get(url, headers=READ_HEADERS)
    return response.json()
