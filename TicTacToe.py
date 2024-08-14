class TicTacToe:
    def __init__(self):
        # Table variables stored in a dictionary, automatically called and created
        self.board = {
            "Tl": " ", "Tm": " ", "Tr": " ",
            "Ml": " ", "Mm": " ", "Mr": " ",
            "Bl": " ", "Bm": " ", "Br": " "
        }
    def print_board(self):
        # Prints a new tic-tac-toe board
        print(" " + self.board["Tl"] + " | " + self.board["Tm"] + " | " + self.board["Tr"] + " ")
        print("---|---|---")
        print(" " + self.board["Ml"] + " | " + self.board["Mm"] + " | " + self.board["Mr"] + " ")
        print("---|---|---")
        print(" " + self.board["Bl"] + " | " + self.board["Bm"] + " | " + self.board["Br"] + " ")
    def update_board(self,choice,symbol):
        if choice in self.board and self.board[choice] == " ":
            self.board[choice] = symbol
            return True
        return False
    def get_random_empty_spot(self):
        import random
        # Collects a list of the empty spots
        empty_spots = [spot for spot, value in self.board.items() if value == " "]
        # Return a random empty spot if available
        return random.choice(empty_spots) if empty_spots else None
    def check_winner(self,player):
        winning_conditions = [
            # Horizontal win
            [self.board["Tl"], self.board["Tm"], self.board["Tr"]],
            [self.board["Ml"], self.board["Mm"], self.board["Mr"]],
            [self.board["Bl"], self.board["Bm"], self.board["Br"]],
            # Vertical win
            [self.board["Tl"], self.board["Ml"], self.board["Bl"]],
            [self.board["Tm"], self.board["Mm"], self.board["Bm"]],
            [self.board["Tr"], self.board["Mr"], self.board["Br"]],
            # Diagonal win
            [self.board["Tl"], self.board["Mm"], self.board["Br"]],
            [self.board["Tr"], self.board["Mm"], self.board["Bl"]]
        ]
        for condition in winning_conditions:
            if condition[0] == condition[1] == condition[2] == player:
                return True
        return False
