# XDA Command Tester

**XDA Command Tester** is a PyQt6-based application designed to interact with and simulate the execution of XDA language commands. This tool allows you to manage and test communication with your local servers, IoT devices, and mock environments by sending commands like `<Start>`, `<Stop>`, `Node(API)`, and more.

### Features
- **XDA Command Simulation**: Execute XDA commands such as `<Start>`, `<Stop>`, and `Node(API)` with a simple GUI.
- **Responsive Design**: The app is designed to be fully responsive, mimicking Apple’s aesthetic with smooth interactions.
- **Mock Server Integration**: Test your commands without needing a real server through mock setups.
- **Real-time Feedback**: Display feedback of command execution status in the app interface.
- **User-Friendly Interface**: A simple and interactive UI to input and execute commands.

### Screenshots

Below is a mock screenshot of the app interface:

![XDA Command Tester](xdadeveloper.png)

### Installation

To run this project on your local machine, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/XevilA/XDA-Language/
    cd XDA-Language
    ```

2. **Install Dependencies**

    Make sure you have `Python 3` and `pip` installed. Then, install the required libraries:

    ```bash
    pip install PyQt6
    ```

3. **Run the Application**

    After installing dependencies, run the app by executing:

    ```bash
    python main.py
    ```

    The app will open up, and you can start testing the XDA commands.

### Commands List

The following XDA commands are supported in the app:

- **Start Node**: `<Start> Node[1]` — Starts the selected node (e.g., a server, IoT device).
- **Stop Node**: `<Stop> Node[1]` — Stops the selected node.
- **Set Node(API)**: `Node(API) = "API_KEY"` — Set the API key for communication with the node.
- **Connect to Node**: `<CONNECT [NodeAPI]>` — Connect to the node via API.
- **Monitor Node Status**: `<STAT (Node[*])>` — Retrieve the status of the node, such as resource usage, OS information, and more.
- **Log Status**: `<LOG (Stat) => "log.txt"` — Logs the status to a file for reporting purposes.
- **System Control (Admin)**: `<SYS>` — Use system control features (Admin only).
- **Send Data**: `<Data>` — Send data to the node (e.g., files, scripts).
- **Kill Process**: `<kill> Node[x]` — Kill a process running on a specific node.
- **Emergency**: `<emer>` — Emergency functions for handling network errors and system failures.

### GUI Features

- **Responsive Layout**: The UI is designed to be responsive and modern, inspired by Apple’s design language.
- **User Input**: A simple input field for API keys and other data.
- **Buttons for Commands**: Buttons to simulate starting and stopping nodes, setting API keys, and more.
- **Feedback Area**: A section in the UI where the output or errors are shown after executing a command.

### Example Command Usage

- To **Start Node**:

    Click the "Start Node" button to execute `<Start> Node[1]`.

- To **Stop Node**:

    Click the "Stop Node" button to execute `<Stop> Node[1]`.

- To **Set Node(API)**:

    Enter the API key in the input field and click the "Set Node(API)" button.

- To **Monitor Node**:

    Click the "Connect to Node" button to simulate monitoring and connection commands.

### Design Notes

The application features modern, **Apple-inspired** design with clean lines and responsive elements. Here are some design specifications:

1. **Borders**: Every UI element has smooth, rounded corners to match the Apple design aesthetic.
2. **Buttons**: Buttons have a subtle hover effect and rounded corners.
3. **Typography**: The text is easy to read and well-spaced for clarity.

### Example Screenshot with Rounded Corners

```markdown
![App Screenshot](.xda-logo.png)
