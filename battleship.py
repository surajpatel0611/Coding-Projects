import random

# Create the game board
board_size = 4
board = [["O" for _ in range(board_size)] for _ in range(board_size)]

# Generate a random location for the battleship
battleship_row = random.randint(0, board_size - 1)
battleship_col = random.randint(0, board_size - 1)

# Loop
for turn in range(4):  # You can change the number of turns
    print(f"Turn {turn + 1}")
    
    # Display the game board
    for row in board:
        print(" ".join(row))
    
    # Ask the player to guess row and collum
    try:
        guess_row = int(input("Guess Row (1-4): ")) - 1
        guess_col = int(input("Guess Col (1-4): ")) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Check the user's input
    if guess_row == battleship_row and guess_col == battleship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row >= board_size) or (guess_col < 0 or guess_col >= board_size):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"

    # End of the game
    if turn == 3:
        print("Game Over")
        print(f"The battleship was at row {battleship_row + 1} and column {battleship_col + 1}")
