import json
from pathlib import Path

from tinydb import TinyDB
from tinydb.middlewares import CachingMiddleware
from tinydb.storages import JSONStorage

BASE_DIR = Path(__file__).resolve().parent.parent


ESMA_SOURCE_JSON = BASE_DIR / "assets" / "esmaul-husna.json"
SURAH_SOURCE_JSON = BASE_DIR / "assets" / "surah.json"

TINYDB_FILE = BASE_DIR / "tinydb_data.json"  # Fichier généré (ignoré dans git)
DB = TinyDB(TINYDB_FILE, storage=CachingMiddleware(JSONStorage))


def fulfill_tinydb_table(db: TinyDB, source: Path, table_name: str):
    if not source.exists():
        msg = f"Fichier source {source} introuvable."
        raise FileNotFoundError(msg)

    with source.open("r") as f:
        json_items = json.load(f)

    tinydb_table = db.table(table_name)
    tinydb_table.insert_multiple(json_items)


def seed_database():
    DB.drop_tables()

    fulfill_tinydb_table(DB, ESMA_SOURCE_JSON, "esma")
    fulfill_tinydb_table(DB, SURAH_SOURCE_JSON, "surah")
