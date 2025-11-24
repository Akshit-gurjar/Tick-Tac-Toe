import tkinter as tk
from gui import TicTacToeApp

if __name__ == "__main__":
    # Initialize the main Tkinter window
    root = tk.Tk()
    
    # Initialize our application
    app = TicTacToeApp(root)
    
    # Run the main event loop
    root.mainloop()