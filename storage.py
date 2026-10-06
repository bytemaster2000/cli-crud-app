import json
import os

FILE = "contacts.json"

def load_data():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Data file corrupted. Starting fresh.")
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)