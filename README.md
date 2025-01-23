# Sudoku Solver 🧩

## Before                                                                                                 

![Image](https://github.com/user-attachments/assets/f328ccfe-549f-41b7-9636-4651adb814f5) 

A simple and efficient Sudoku Solver built using Python and Tkinter. This project provides a graphical user interface (GUI) that allows users to input a Sudoku puzzle and solve it using a backtracking algorithm.

## Features
- **Sudoku Solver:** Solves a given Sudoku puzzle using a backtracking algorithm.
- **Interactive GUI:** Users can input the Sudoku puzzle directly into the grid.
- **Validation:** Before solving, the board is checked for validity.
- **Navigation:** Keyboard arrow keys are enabled for easy movement across the grid.
- **Reset Functionality:** A reset button is available to clear the input board.

## Installation

To run the Sudoku Solver on your local machine, follow the steps below:

### Requirements
- Python 3.x
- Tkinter (comes pre-installed with Python)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sudoku-solver.git

2. Run the sudoku_solver.py file:
   ```bash
   python sudoku_solver.py

## Usage
- Open the application, and the Sudoku board will appear in a grid format.
- Enter the Sudoku puzzle into the grid.
- Click the Solve Sudoku button to find the solution.
- If the puzzle is solvable, the solved grid will be displayed.
- You can reset the board by clicking the Reset button.

## Backtracking Algorithm
- The Sudoku puzzle is solved using a backtracking algorithm, which attempts to fill the empty cells with numbers from 1 to 9. It checks whether a number can be placed in a particular cell based on the Sudoku rules (no duplicates in rows, columns, or 3x3 subgrids). If the solution fails, the algorithm backtracks and tries another number.

## Built with 🐍 and ❤️ using Python and Tkinter

### Acknowledgment

Under guidance of [ Dr Agughasi Victor Ikechukwu](https://github.com/Victor-Ikechukwu)
