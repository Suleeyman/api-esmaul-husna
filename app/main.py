from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from tinydb import Query, TinyDB

from app.db import import_json_to_tinydb

import_json_to_tinydb()
app = FastAPI(title="API Esmaul Husna")
app.mount("/images", StaticFiles(directory="assets/static/images"), name="static")
app.mount("/audio", StaticFiles(directory="assets/static/audio"), name="static")

# --- Configuration de TinyDB ---
DB_PATH = Path("tinydb_data.json")
db = TinyDB(DB_PATH)
Item = Query()


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "API Esmaul Husna",
        "link": "https://github.com/Suleeyman/api-esmaul-husna",
    }


@app.get("/esmas")
def say_hello():
    return db.all()


@app.get("/esmas/{esma_id}")
def get_item_by_id(esma_id: str):
    result = db.search(esma_id == Item.id)
    if not result:
        raise HTTPException(status_code=404, detail="Item not found")
    return result[0]
