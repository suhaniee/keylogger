Simple Python Keylogger

This is a basic Python keylogger built using the `pynput` library. It captures every key pressed on the keyboard and saves it into a text file (`log.txt`).

📜 Features

* Logs all keystrokes (letters, numbers, and symbols).
* Detects and replaces special keys like:

  * Space → ' '
  * Enter → newline
  * Backspace → deletes the last character in the log file
* Stores data in a file named **`log.txt`** in the same directory.



Requirements

Make sure Python is installed on your system.

Install the required library:

bash
pip install pynput

How to Run

1. Save the script as `keylogger.py`.
2. Open your terminal or command prompt in the same folder.
3. Run the script:

  bash
   python keylogger.py

4. The program will start listening for keyboard input and log everything to `log.txt`.

How It Works

* The program uses the `pynput.keyboard.Listener` class to monitor key presses.
* Each keystroke is processed by the `writetofile()` function and written to `log.txt`.
* Backspace is handled separately by reopening and editing the log file to remove the last character.

Disclaimer

This project is **for educational purposes only**.
Do **not** use it on systems or devices you do not own or have permission to monitor.
Unauthorized use may violate privacy laws and ethical guidelines.

Example Output

If you type:

Hello World!

Your `log.txt` file will contain:

Hello World!


