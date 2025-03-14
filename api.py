# mesh_commander/api.py
from flask import Blueprint, jsonify, request
from mesh_commander.core import MeshCommanderPlugin
from mesh_commander import mesh_api

blueprint = Blueprint('mesh_commander_api', __name__)

@blueprint.route('/nodes', methods=['GET'])
def get_nodes():
    plugin = MeshCommanderPlugin()
    return jsonify({node_id: node.__dict__ for node_id, node in plugin.nodes.items()})

@blueprint.route('/nodes/<node_id>/message', methods=['POST'])
def send_message(node_id):
    plugin = MeshCommanderPlugin()
    message = request.json['message']
    node = plugin.nodes.get(node_id)
    if node:
        mesh_api.send_message(node.serial_port, message)
        return jsonify({"result": "message sent"})
    return jsonify({"result": "node not found"})

@blueprint.route('/nodes/<node_id>/channel', methods=['POST'])
def set_channel(node_id):
    plugin = MeshCommanderPlugin()
    channel_settings = request.json['channel_settings']
    node = plugin.nodes.get(node_id)
    if node:
        mesh_api.set_channel(node.serial_port, channel_settings)
        return jsonify({"result": "channel set"})
    return jsonify({"result": "node not found"})
