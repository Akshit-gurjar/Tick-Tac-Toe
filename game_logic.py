import random

def check_winner(board):
    """
    Checks the board for a winner.
    Returns 'X', 'O', 'Draw', or None (if game continues).
    """
    # All possible winning combinations (rows, cols, diagonals)
    winning_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]

    for a, b, c in winning_combos:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]

    if "" not in board:
        return "Draw"
    
    return None

def get_computer_move(board, difficulty="easy"):
    """
    Returns the index (0-8) where the computer wants to move.
    """
    available_moves = [i for i, x in enumerate(board) if x == ""]
    
    if not available_moves:
        return None

    # Simple AI: Just picks a random available spot
    # You can expand this section to implement Minimax for an unbeatable AI
    return random.choice(available_moves)