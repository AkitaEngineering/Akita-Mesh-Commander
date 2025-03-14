# mesh_commander/mesh_api.py
import serial
import time

def get_node_status(serial_port):
    try:
        ser = serial.Serial(serial_port, 115200, timeout=5)
        ser.write(b"!info\r\n")
        time.sleep(1)
        response = ser.read_all().decode()
        ser.close()

        if not response:
            return None

        if "Type: Router" in response:
            node_type = "router"
        elif "Type: Client" in response:
            node_type = "client"
        else:
            node_type = "unknown"

        location = (0, 0)
        channel = "unknown"
        battery = 0

        return {"type": node_type, "location": location, "channel": channel, "battery": battery}

    except serial.SerialException as e:
        print(f"Error communicating with {serial_port}: {e}")
        return None
    except Exception as e:
        print(f"Error parsing response from {serial_port}: {e}")
        return None

def send_message(serial_port, message):
    try:
        ser = serial.Serial(serial_port, 115200, timeout=5)
        ser.write(f"!sendtext {message}\r\n".encode())
        ser.close()
        return True
    except serial.SerialException as e:
        print(f"Error sending message to {serial_port}: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error while sending message: {e}")
        return False

def set_channel(serial_port, channel_settings):
    try:
        ser = serial.Serial(serial_port, 115200, timeout=5)
        print(f"Setting channel on {serial_port}: {channel_settings}")
        ser.close()
        return True
    except serial.SerialException as e:
        print(f"Error setting channel on {serial_port}: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error while setting channel: {e}")
        return False

def get_nodes_in_mesh(config):
    return config.get("nodes", [])
