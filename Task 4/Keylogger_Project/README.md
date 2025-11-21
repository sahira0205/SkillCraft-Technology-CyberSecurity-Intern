
# Basic Keylogger - Task 04

This repository contains a Python script that implements a basic keylogger as part of the Cyber Security Internship at SkillCraft Technology. The program captures keystrokes and saves them to a log file, demonstrating how keystroke logging works for educational and diagnostic purposes.

## ⚠️ Ethical Disclaimer
**For Educational Purposes Only.**
This project was created strictly for learning and understanding cybersecurity concepts. Keyloggers can be used maliciously to steal sensitive data. Using this software on devices without the explicit permission of the owner is illegal and unethical. The author declines any responsibility for the misuse of this tool.

## Features
- **Keystroke Logging:** Captures all keys pressed on the keyboard.
- **Readable Output:** Automatically formats special keys (Space, Enter, Tab) to create readable sentences rather than raw key codes.
- **Session Tracking:** Records the start and end timestamps for every logging session.
- **Clean Logs:** Uses a text file (`keylog.txt`) to store the captured data.
- **Stealth Mode (Basic):** Runs in the background of the terminal until manually stopped.

## Prerequisites
To run this project, you need:
- **Python 3.x** installed on your system.
- The `pynput` library.

## Installation

1. Clone this repository or download the `keylogger.py` file.
2. Open your terminal or command prompt.
3. Install the required dependency:
   ```bash
   pip install pynput
````

## Usage

1.  Navigate to the project directory:

    ```bash
    cd path/to/your/folder
    ```

2.  Run the script:

    ```bash
    python keylogger.py
    ```

3.  **Start Typing:** The script is now listening. You can type in any application (Notepad, Browser, etc.).

4.  **Stop Logging:** Press the `ESC` key to stop the recording and save the session.

5.  **View Logs:** Open the `keylog.txt` file generated in the same directory to view the captured keystrokes.

## Program Flow (How it Works)

1.  **Start:** The program initiates and imports the `pynput` and `datetime` libraries.
2.  **Initialization:** It creates/opens the log file and gets the current system time.
3.  **Session Header:** Writes a "New Session Started" header with the timestamp.
4.  **Listening Loop:** The code enters a loop, constantly waiting for keyboard input.
5.  **Key Capture & Formatting:**
      - If a standard key (letters/numbers) is pressed, it logs the character.
      - If a special key (Space, Enter) is pressed, it converts it to readable text (e.g., a real space or new line).
6.  **Stop Condition:** If the **ESC** key is pressed, the program writes the "End Time" timestamp and terminates.

## Output Example

The `keylog.txt` file will look like this:

```text
==============================
 NEW SESSION STARTED: 2025-11-21 10:05:00
==============================

Hello, this is a test of the keylogger project.
It captures [SHIFT] Special characters and new lines.

[Session Ended: 2025-11-21 10:05:45]
==============================
```

## Technologies Used

  - **Python**: Primary programming language.
  - **pynput**: Library used to control and monitor input devices.
  - **datetime**: Module used for timestamping sessions.

