# mesh_commander/utils.py

import logging
import json
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_json_file(filepath):
    """Loads and parses a JSON file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        return None
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in {filepath}")
        return None
    except Exception as e:
        logger.error(f"Error loading {filepath}: {e}")
        return None

def save_json_file(data, filepath):
    """Saves data to a JSON file."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info(f"Saved data to {filepath}")
        return True
    except Exception as e:
        logger.error(f"Error saving to {filepath}: {e}")
        return False

def ensure_directory_exists(directory):
    """Creates a directory if it does not exist."""
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logger.info(f"Created directory: {directory}")
        return True
    except Exception as e:
        logger.error(f"Error creating directory {directory}: {e}")
        return False

def handle_serial_error(e, serial_port):
    """Handles serial communication errors."""
    logger.error(f"Serial communication error on {serial_port}: {e}")
    return None

def handle_meshtastic_response_error(e, response):
    """Handles errors when parsing meshtastic responses."""
    logger.error(f"Error parsing Meshtastic response: {e}, Response: {response}")
    return None

def handle_api_error(e, message="API Error"):
    """Handles api errors."""
    logger.error(f"{message}: {e}")
    return {"error": str(e)}, 500 #return an error message and a 500 error code.
