# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_win(board, player):
    # Check rows for a win
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns for a win
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals for a win
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to play Tic-Tac-Toe
def tic_tac_toe():
    # Initialize an empty 3x3 board
    board = [[" " for _ in range(3)] for _ in range(3)]

    # Start with player 'X'
    player = "X"

    # Main game loop
    for _ in range(9):
        # Display the current game board
        print_board(board)

        # Input and validation loop for player moves
        while True:
            try:
                row, col = map(int, input(f"Player {player}, enter row and column (0-2) separated by space: ").split())
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    break
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

        # Update the board with the player's move
        board[row][col] = player

        # Check if the current player has won
        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return

        # Switch to the other player for the next turn
        player = "O" if player == "X" else "X"

    # If all moves are exhausted and no winner is declared, it's a draw
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
