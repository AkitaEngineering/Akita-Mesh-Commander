# mesh_commander/core.py
from akita.plugins import AkitaPlugin
from flask import Flask, jsonify
from mesh_commander import api, models, mesh_api, config, utils

class MeshCommanderPlugin(AkitaPlugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = Flask(__name__)
        self.app.register_blueprint(api.blueprint)
        self.nodes = {}
        self.config = config.load_config()
        self.discover_mesh()

    def discover_mesh(self):
        node_list = mesh_api.get_nodes_in_mesh(self.config)
        for node in node_list:
            serial_port = node["serial_port"]
            node_id = node["node_id"]
            status = mesh_api.get_node_status(serial_port)
            if status:
                self.nodes[node_id] = models.Node(node_id, serial_port, status["type"], status["location"], status["channel"], status["battery"])

    def run(self):
        self.app.run(debug=True, port=5003)
