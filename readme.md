🧩 Sudoku Master: CSP Solver & Interactive Game
A Python-based graphical desktop application built with Tkinter that demonstrates how Artificial Intelligence solves Sudoku using Constraint Satisfaction Problem (CSP) algorithms.

Beyond just an AI solver, this project also features a fully interactive User Mode that allows human players to solve puzzles with real-time validation and smart hints.

✨ Features
🎮 Two Play Modes
Full Solve Mode: Watch the AI solve the puzzle instantly. Compares the execution time of different algorithms so you can see which one is more efficient.

User Solve Mode: Play the Sudoku yourself! Features an interactive grid with real-time feedback:

🟢 Green: Correct number.

🔴 Red: Incorrect number.

🟣 Purple: Hint provided by the system.

🧠 Advanced AI Algorithms
Simple Backtracking: A depth-first search algorithm that "guesses" numbers and backtracks when it hits a dead end.

AC-3 (Arc Consistency 3): An advanced CSP technique that pre-filters impossible numbers from each cell's "domain" before making guesses, drastically reducing the search space and execution time.

🛠️ Smart UI/UX
Dynamic cell highlighting on mouse hover/focus.

Smart "Hint" system that detects the currently selected cell and prevents overwriting locked puzzle values.

Automatic background processing: solves the puzzle silently in the background to provide accurate, real-time validation to the user.

## 📂 Project Structure

* **`main.py`** - The entry point of the application. Run this file to start the game!
* **`GUI.py`** - Handles the Tkinter interface, routing, event binding, and user validations.
* **`Backtrack.py`** - Contains the logic for the basic Backtracking solver.
* **`AC3.py`** - Contains the logic for the MAC (Maintaining Arc Consistency) solver.
* **`grid.py`** - Handles setting up the initial CSP Variables, Domains, and Constraints.
* **`Puzzles/`** - A directory containing text files of starting Sudoku grids categorized by difficulty (Easy, Medium, High).
* **`bg.jpg`** - Background image asset for the main menu.

---

## 🚀 Installation & Setup

### Prerequisites
* Python 3.x installed on your machine.
* `Pillow` library (for rendering the background image).

### Steps to Run
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/Sudoko_Graphical_User_Interface.git](https://github.com/yourusername/Sudoko_Graphical_User_Interface.git)
   cd Sudoku-CSP-Solver
Install dependencies:

Bash
pip install Pillow
Run the application:

Bash
python main.py