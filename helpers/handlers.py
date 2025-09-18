import json
import os

DB_FILE = "databases/data.json"

def load_db():
    if not os.path.exists(DB_FILE):
        # Agar file missing hai to create kar do with empty structure
        with open(DB_FILE, "w") as f:
            json.dump({"users": []}, f, indent=4)

    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)
