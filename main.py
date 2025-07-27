from fastapi import FastAPI, HTTPException
from pathlib import Path
from tinydb import TinyDB, Query
from db import import_json_to_tinydb

import_json_to_tinydb()
app = FastAPI()

# --- Configuration de TinyDB ---
DB_PATH = Path("tinydb_data.json")
db = TinyDB(DB_PATH)
Item = Query()

@app.get("/")
def root():
    return {"message": "API Esmaul Husnas", "link": "https://github.com/Suleeyman/api-esmaul-husna"}

@app.get("/esmas")
def say_hello():
    return db.all()

@app.get("/esmas/{esma_id}")
def get_item_by_id(esma_id: str):
    result = db.search(esma_id == Item.id)
    if not result:
        raise HTTPException(status_code=404, detail="Item not found")
    return result[0]