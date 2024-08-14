from TicTacToe import TicTacToe

# Initial game conditions
game = TicTacToe()
gameStarted = False
gameOver = False

# Prompts the user to play
print("Wanna play Tic Tac Toe?")

response = input().lower().strip()
valid_responses = {"yes","y","yeah","sure","i guess","might as well","fine","okay","ok","yes please"}
if response in valid_responses:
    print("Yay! Go ahead and go first!")
else:
    print("Too bad!")

game.print_board()  # Prints a new tic-tac-toe board
gameStarted = True

if gameStarted:
    while not gameOver:
        # Player's turn
        choice = input("Enter your move: (e.g., 'tl' for top-left, 'mm' for middle-middle, 'br' for bottom-right) ").lower()
        if game.update_board(choice.capitalize(), "X"):
            game.print_board()
        else:
            print("Invalid move. Try again.")
            continue

        # Check if player won
        if game.check_winner("X"):
            gameOver = True
            print("Hey! You cheated!")
            break

        # Computer's turn
        random_spot = game.get_random_empty_spot()
        if random_spot: #if it exists
            game.update_board(random_spot, "O")
            print("Okay.. your move!")
            game.print_board()

            # Check if computer won
            if game.check_winner("O"):
                gameOver = True
                print("How did you lose to a stupid computer? What a loser!")
                break

        # If there are no available spots, the game must have ended in a tie
        if not any(value == " " for value in game.board.values()):
            print("Looks like it's a tie!")
            gameOver = True
