# mesh_commander/config.py
import json

def load_config(filepath="config.json"):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Configuration file not found: {filepath}")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filepath}")
        return {}
