# Akita Mesh Commander

Akita Mesh Commander is an Akita Engineering plugin designed to manage Meshtastic-based mesh networks. It provides tools to monitor, control, and configure devices within a Meshtastic mesh.

## Features

* **Node Management:**
    * Discover and monitor Meshtastic nodes.
    * Retrieve node status (type, location, channel, battery).
* **Message Handling:**
    * Send messages to individual nodes.
* **Configuration Control:**
    * Set channel configurations for nodes.
* **Extensible Design:**
    * Modular architecture for easy expansion and customization.
* **Basic Configuration:**
    * Configuration through a `config.json` file.
* **Error Handling:**
    * Improved error handling for serial communications and JSON parsing.
    * API error handling.
* **Utility functions:**
    * Logging.
    * JSON file handling.
    * Directory creation.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [repository_url]
    cd akita-mesh-commander
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the plugin:**

    ```bash
    pip install -e .
    ```

4.  **Install Pyserial:**

    ```bash
    pip install pyserial
    ```

5.  **Configuration:**
    * Create a `config.json` file in the base directory of the plugin. An example is provided below.
    ```json
    {
      "nodes": [
        {"serial_port": "/dev/ttyUSB0", "node_id": "node1"},
        {"serial_port": "/dev/ttyUSB1", "node_id": "node2"}
      ]
    }
    ```
    * Adjust the serial port names to match your system.

## Usage

* This plugin is designed to be integrated with the Akita Engineering platform. Refer to the Akita documentation for plugin integration instructions.
* To test the api outside of the akita framework, you can run the core.py file directly.
    * `python mesh_commander/core.py`
* The API will be available on port 5003 by default.
* API endpoints:
    * `/nodes` (GET): Retrieves a list of nodes.
    * `/nodes/<node_id>/message` (POST): Sends a message to a node.
    * `/nodes/<node_id>/channel` (POST): Sets the channel configuration for a node.

## Important Notes

* **Meshtastic Communication:** The `mesh_api.py` module contains placeholder code for Meshtastic device communication. You will need to replace this with code that matches your specific Meshtastic setup and firmware.
* **Akita Integration:** This plugin must be integrated with the Akita Engineering platform to function correctly.
* **Serial Ports:** Ensure that the serial port names in the `config.json` file are correct.
* **Error Handling:** While error handling has been improved, further testing and refinement are recommended.
* **Security:** Implement appropriate security measures for production environments.
* **UI:** A user interface is not included in this release.
* **Node Discovery:** The current node discovery method is basic. Implement a more robust discovery mechanism for larger networks.
* **Meshtastic Command Parsing:** The parsing of meshtastic responses within the `mesh_api.py` file needs to be adjusted to match the output of your specific meshtastic firmware.

## Contributing

Contributions are welcome! Please submit pull requests or bug reports to the repository.
