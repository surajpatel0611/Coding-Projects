import random

# Create the game board
board = [["O" for _ in range(5)] for _ in range(5)]

# Generate a random location for the battleship
battleship_row = random.randint(0, 4)
battleship_col = random.randint(0, 4)

# Game loop
for turn in range(10):  # You can change the number of turns
    print(f"Turn {turn + 1}")
    
    # Display the game board
    for row in board:
        print(" ".join(row))
    
    # Ask the player for a guess
    try:
        guess_row = int(input("Guess Row (0-4): "))
        guess_col = int(input("Guess Col (0-4): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Check the guess
    if guess_row == battleship_row and guess_col == battleship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"

    # End of the game
    if turn == 3:
        print("Game Over")
        print(f"The battleship was at row {battleship_row} and column {battleship_col}")
