# mesh_commander/models.py
class Node:
    def __init__(self, node_id, serial_port, type, location, channel, battery):
        self.node_id = node_id
        self.serial_port = serial_port
        self.type = type
        self.location = location
        self.channel = channel
        self.battery = battery
