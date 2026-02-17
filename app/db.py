import json
from pathlib import Path

from tinydb import TinyDB

BASE_DIR = Path(__file__).resolve().parent.parent


SOURCE_JSON = BASE_DIR / "assets" / "esmaul-husna.json"  # Ton fichier versionné
TINYDB_FILE = BASE_DIR / "tinydb_data.json"  # Fichier généré (ignoré dans git)


def import_json_to_tinydb() -> None:
    # Ne réécrit que si esmaul-husna.json existe
    p = Path(SOURCE_JSON)
    if not p.exists():
        msg = f"Fichier source {SOURCE_JSON} introuvable."
        raise FileNotFoundError(msg)

    with p.open("r") as f:
        items = json.load(f)

    db = TinyDB(TINYDB_FILE)
    db.drop_tables()  # Nettoie les anciennes données
    db.insert_multiple(items)

    db.close()
