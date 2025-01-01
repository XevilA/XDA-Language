import re
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QWidget, QLabel, QFileDialog
)
from PyQt6.QtCore import Qt


class XDAInterpreter:
    def __init__(self):
        self.node_api = None
        self.nodes = {}
        self.log_file = "log.txt"
        self.output = []

    def parse_xda(self, xda_script):
        commands = re.findall(r"<(.*?)>", xda_script)
        for command in commands:
            self.execute_command(command)

    def execute_command(self, command):
        if command.startswith("Start("):
            self.start_engine(command)
        elif command.startswith("Stop("):
            self.stop_nodes(command)
        elif "NodeAPI" in command:
            self.set_node_api(command)
        elif command.startswith("Conect"):
            self.connect_node()
        elif command.startswith("Stat"):
            self.stat_node(command)
        elif command.startswith("LOG"):
            self.log_stat(command)
        elif command.startswith("out"):
            self.export_file(command)
        elif command.startswith("short"):
            self.compress_data()
        elif command.startswith("alone"):
            self.standalone_module(command)
        elif command.startswith("send"):
            self.send_argument(command)

    def start_engine(self, command):
        match = re.search(r"node\[(\d+)\]", command)
        if match:
            node_id = int(match.group(1))
            self.nodes[node_id] = {"status": "started"}
            self.output.append(f"Engine started for node {node_id}.")

    def stop_nodes(self, command):
        if "node [*]" in command:
            for node_id in self.nodes:
                self.nodes[node_id]["status"] = "stopped"
            self.output.append("All nodes stopped.")

    def set_node_api(self, command):
        match = re.search(r"NodeAPI\s*=\s*\"(.*?)\"", command)
        if match:
            self.node_api = match.group(1)
            self.output.append(f"NodeAPI set to {self.node_api}.")

    def connect_node(self):
        if self.node_api:
            self.output.append(f"Connecting nodes with API: {self.node_api}.")
        else:
            self.output.append("NodeAPI is not set. Unable to connect.")

    def stat_node(self, command):
        if "Node[*]" in command:
            self.output.append("Node statistics:")
            for node_id, node_data in self.nodes.items():
                self.output.append(f"Node {node_id}: {node_data}")
        else:
            self.output.append("Invalid Stat command.")

    def log_stat(self, command):
        if "LOG" in command:
            with open(self.log_file, "w") as log:
                for node_id, node_data in self.nodes.items():
                    log.write(f"Node {node_id}: {node_data}\n")
            self.output.append(f"Node statistics logged to {self.log_file}.")

    def export_file(self, command):
        match = re.search(r"out\s*=>\s*\"(.*?)\"", command)
        if match:
            file_name = match.group(1)
            with open(file_name, "w") as file:
                file.write("\n".join(self.output))
            self.output.append(f"Output exported to {file_name}.")

    def compress_data(self):
        self.output = [line.strip() for line in self.output]
        self.output.append("Output data compressed.")

    def standalone_module(self, command):
        self.output.append("Standalone module created. Cannot connect to others.")

    def send_argument(self, command):
        match = re.search(r"send\s*\((.*?)\)", command)
        if match:
            argument = match.group(1)
            self.output.append(f"Sent argument: {argument}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("XDA Language Simulator")
        self.setGeometry(100, 100, 800, 600)
        self.interpreter = XDAInterpreter()
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # Input Text Editor
        self.input_editor = QTextEdit()
        self.input_editor.setPlaceholderText("Write your XDA script here...")
        layout.addWidget(QLabel("XDA Script:"))
        layout.addWidget(self.input_editor)

        # Output Display
        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        layout.addWidget(QLabel("Output:"))
        layout.addWidget(self.output_display)

        # Buttons
        button_layout = QHBoxLayout()
        self.run_button = QPushButton("Run")
        self.run_button.clicked.connect(self.run_script)
        button_layout.addWidget(self.run_button)

        self.export_button = QPushButton("Export Output")
        self.export_button.clicked.connect(self.export_output)
        button_layout.addWidget(self.export_button)

        layout.addLayout(button_layout)
        central_widget.setLayout(layout)

    def run_script(self):
        script = self.input_editor.toPlainText()
        self.interpreter.output.clear()
        self.interpreter.parse_xda(script)
        self.output_display.setText("\n".join(self.interpreter.output))

    def export_output(self):
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        file_dialog.setNameFilter("Text Files (*.txt)")
        if file_dialog.exec():
            file_name = file_dialog.selectedFiles()[0]
            with open(file_name, "w") as file:
                file.write(self.output_display.toPlainText())
            self.output_display.append(f"Output exported to {file_name}")


# Run Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
