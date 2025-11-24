# 🎮 Python Tic-Tac-Toe (GUI)

A clean, modular Tic-Tac-Toe game built using **Python** and **Tkinter**. This project features a graphical user interface and allows users to play against a friend or challenge the computer.

## ✨ Features
* **Graphical Interface:** User-friendly window using Python's built-in `tkinter` library.
* **Two Game Modes:**
    * **Play vs Friend:** Classic hot-seat multiplayer.
    * **Play vs Computer:** Single-player mode against a basic AI.
* **Modular Design:** Code is split into Logic, GUI, and Main execution for better readability and maintenance.
* **Game State Handling:** Includes win detection, draw detection, and turn switching.

## 📂 Project Structure

The project is divided into three specific modules:

1.  `main.py`: **The Entry Point.** This file initializes the application and starts the main loop.
2.  `gui.py`: **The Interface.** Handles the window creation, buttons, menu navigation, and updates the display.
3.  `game_logic.py`: **The Brain.** Contains the rules of the game (win checking) and the Computer AI logic.

## 🚀 Getting Started

### Prerequisites
* **Python 3.13** installed on your system.
* *Note: Tkinter is included with standard Python installations on Windows and macOS. Linux users might need to install it (e.g., `sudo apt-get install python3-tk`).*

### Installation
1.  Create a new folder on your computer.
2.  Download or create the three files (`main.py`, `gui.py`, `game_logic.py`) inside this folder.

### How to Run
Open your terminal or command prompt, navigate to the project folder, and run:

```
python main.py
```