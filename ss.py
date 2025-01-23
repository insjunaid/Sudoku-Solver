import tkinter as tk
from tkinter import messagebox

def print_board(board):
    """Prints the Sudoku board in a readable format."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end=" ")

def find_empty_cell(board):
    """Finds an empty space in the Sudoku board (marked by 0)."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(board, num, pos):
    """Checks if placing 'num' at position 'pos' is valid."""
    row, col = pos

    # Check row
    for j in range(9):
        if board[row][j] == num and j != col:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num and i != row:
            return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve_sudoku(board):
    """Solves the Sudoku board using backtracking."""
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # No empty spaces, puzzle solved!

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):  # Recursively try solving
                return True

            board[row][col] = 0  # Backtrack

    return False  # No solution found

def get_board_from_gui():
    """Retrieves the Sudoku board from the Tkinter input fields."""
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            value = entries[i][j].get()
            row.append(int(value) if value.isdigit() and value != '' else 0)
        board.append(row)
    return board

def is_board_valid(board):
    """Checks if the current board configuration is valid before solving."""
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != 0:
                board[i][j] = 0  # Temporarily remove the number
                if not is_valid(board, num, (i, j)):
                    return False
                board[i][j] = num  # Restore the number
    return True

def solve_from_gui():
    """Solves the Sudoku board from the GUI input with validation."""
    board = get_board_from_gui()

    # Validate board before solving
    if not is_board_valid(board):
        messagebox.showerror("Sudoku Solver", "The given Sudoku board is invalid!")
        return
    
    if solve_sudoku(board):
        update_gui_board(board)
        messagebox.showinfo("Sudoku Solver", "Sudoku solved successfully!")
    else:
        messagebox.showerror("Sudoku Solver", "No solution exists for the given Sudoku.")

def reset_board():
    """Clears all input fields to reset the Sudoku grid."""
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].config(bg="white")

def update_gui_board(board):
    """Updates the Tkinter grid with the solved Sudoku."""
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, str(board[i][j]))
            entries[i][j].config(bg="#d4edda")  # Light green for solved numbers

def move_cursor(event, row, col):
    """Handles keyboard navigation with arrow keys."""
    if event.keysym == "Up" and row > 0:
        entries[row - 1][col].focus()
    elif event.keysym == "Down" and row < 8:
        entries[row + 1][col].focus()
    elif event.keysym == "Left" and col > 0:
        entries[row][col - 1].focus()
    elif event.keysym == "Right" and col < 8:
        entries[row][col + 1].focus()

def create_sudoku_gui():
    """Creates the Sudoku input GUI using Tkinter with enhanced graphics."""
    global entries
    root = tk.Tk()
    root.title("Sudoku Solver")

    root.configure(bg="#2c3e50")  # Background color

    entries = []
    for i in range(9):
        row_entries = []
        for j in range(9):
            entry = tk.Entry(root, width=3, font=('Arial', 18, 'bold'), justify='center', bd=2, relief="solid")
            entry.grid(row=i, column=j, padx=(3 if j % 3 == 0 else 1), pady=(3 if i % 3 == 0 else 1))

            # Thick borders for 3x3 subgrids
            if i in [2, 5]:
                entry.grid(pady=(3, 5))
            if j in [2, 5]:
                entry.grid(padx=(3, 5))

            # Background for easier reading
            if (i // 3 + j // 3) % 2 == 0:
                entry.config(bg="#ecf0f1")  # Light gray
            else:
                entry.config(bg="white")

            # Bind keyboard arrow keys
            entry.bind("<Up>", lambda event, r=i, c=j: move_cursor(event, r, c))
            entry.bind("<Down>", lambda event, r=i, c=j: move_cursor(event, r, c))
            entry.bind("<Left>", lambda event, r=i, c=j: move_cursor(event, r, c))
            entry.bind("<Right>", lambda event, r=i, c=j: move_cursor(event, r, c))

            row_entries.append(entry)
        entries.append(row_entries)

    # Solve button with improved styling
    solve_button = tk.Button(root, text="Solve Sudoku", command=solve_from_gui, 
                             font=('Arial', 14, 'bold'), bg="#27ae60", fg="white", bd=5, relief="ridge")
    solve_button.grid(row=9, column=0, columnspan=4, pady=10, padx=5, sticky="ew")

    # Reset button with improved styling
    reset_button = tk.Button(root, text="Reset", command=reset_board, 
                             font=('Arial', 14, 'bold'), bg="#e74c3c", fg="white", bd=5, relief="ridge")
    reset_button.grid(row=9, column=5, columnspan=4, pady=10, padx=5, sticky="ew")

    root.mainloop()

if __name__ == "__main__":
    create_sudoku_gui()
