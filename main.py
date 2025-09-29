from fastapi import FastAPI, HTTPException
from pathlib import Path
from tinydb import TinyDB, Query
from db import import_json_to_tinydb
from fastapi.staticfiles import StaticFiles

import_json_to_tinydb()
app = FastAPI(title="API Esmaul Husna")
app.mount("/audio", StaticFiles(directory="resources/static/audio"), name="static")

# --- Configuration de TinyDB ---
DB_PATH = Path("tinydb_data.json")
db = TinyDB(DB_PATH)
Item = Query()


@app.get("/")
def root():
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
