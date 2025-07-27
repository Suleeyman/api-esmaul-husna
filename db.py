from tinydb import TinyDB
import json
import os

SOURCE_JSON = "resources/esmaul-husna.json"   # Ton fichier lisible et versionné
TINYDB_FILE = "tinydb_data.json"  # Fichier généré (non versionné)

def import_json_to_tinydb():
    # Ne réécrit que si esmaul-husna.json existe
    if not os.path.exists(SOURCE_JSON):
        raise FileNotFoundError(f"Fichier source {SOURCE_JSON} introuvable.")

    with open(SOURCE_JSON) as f:
        items = json.load(f)

    db = TinyDB(TINYDB_FILE)
    db.drop_tables()  # Nettoie les anciennes données
    db.insert_multiple(items)

    print(f"✅ Importation de {len(items)} objets dans {TINYDB_FILE}")
    db.close()
