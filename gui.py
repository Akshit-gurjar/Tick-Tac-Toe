import tkinter as tk
from tkinter import messagebox
import game_logic  # Importing our logic module

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x450")
        
        # Game State Variables
        self.turn = 'X'
        self.board = [""] * 9
        self.game_mode = None  # 'friend' or 'computer'
        self.game_over = False

        self.create_menu()

    def create_menu(self):
        """Creates the initial selection menu."""
        self.clear_window()
        
        title = tk.Label(self.root, text="Tic Tac Toe", font=("Arial", 24, "bold"))
        title.pack(pady=20)

        btn_friend = tk.Button(self.root, text="Play vs Friend", font=("Arial", 14), 
                               width=20, command=lambda: self.start_game("friend"))
        btn_friend.pack(pady=10)

        btn_computer = tk.Button(self.root, text="Play vs Computer", font=("Arial", 14), 
                                 width=20, command=lambda: self.start_game("computer"))
        btn_computer.pack(pady=10)

    def start_game(self, mode):
        """Sets up the game board."""
        self.game_mode = mode
        self.turn = 'X'
        self.board = [""] * 9
        self.game_over = False
        self.clear_window()
        self.create_board()

    def create_board(self):
        """Draws the 3x3 grid."""
        # Top Info Bar
        self.info_label = tk.Label(self.root, text=f"Player {self.turn}'s Turn", font=("Arial", 14))
        self.info_label.pack(pady=10)

        # Grid Frame
        frame = tk.Frame(self.root)
        frame.pack()

        self.buttons = []
        for i in range(9):
            btn = tk.Button(frame, text="", font=("Arial", 20, "bold"), width=5, height=2,
                            command=lambda idx=i: self.on_click(idx))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

        # Back Button
        back_btn = tk.Button(self.root, text="Back to Menu", command=self.create_menu)
        back_btn.pack(pady=20)

    def on_click(self, index):
        """Handles button clicks."""
        if self.board[index] == "" and not self.game_over:
            # Player Move
            self.make_move(index, self.turn)
            
            # Check if game ended after player move
            if not self.game_over and self.game_mode == "computer" and self.turn == 'O':
                self.root.after(500, self.computer_turn) # Small delay for realism

    def computer_turn(self):
        """Executes computer move."""
        move = game_logic.get_computer_move(self.board)
        if move is not None:
            self.make_move(move, 'O')

    def make_move(self, index, player):
        """Updates internal state and UI."""
        self.board[index] = player
        self.buttons[index].config(text=player, fg="blue" if player == "X" else "red")
        
        winner = game_logic.check_winner(self.board)
        
        if winner:
            self.end_game(winner)
        else:
            # Switch turns
            self.turn = 'O' if self.turn == 'X' else 'X'
            self.info_label.config(text=f"Player {self.turn}'s Turn")

    def end_game(self, result):
        """Handles Win/Draw scenarios."""
        self.game_over = True
        if result == "Draw":
            msg = "It's a Draw!"
        else:
            msg = f"Player {result} Wins!"
        
        messagebox.showinfo("Game Over", msg)
        self.create_menu()

    def clear_window(self):
        """Helper to clear the screen when switching views."""
        for widget in self.root.winfo_children():
            widget.destroy()