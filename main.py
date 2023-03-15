
"""
Ascii Noughts and Crosses Game by Gabriel Lancaster-West
├── Board
│   ├── __init__(size, player_1_symbol, player_2_symbol) -> Initializes a new game board
│   ├── display() -> Displays the current game board
│   ├── make_move(move, player) -> Makes a move on the game board
│   ├── is_valid_move(move) -> Validates if the move is valid or not
│   ├── is_full() -> Determines if the game board is full or not
│   ├── is_winner(player) -> Determines if the player has won the game
│   └── get_size() -> Returns the size of the game board
└── Game
    ├── __init__(size) -> Initializes a new game with a game board of given size
    ├── get_move(player) -> Asks the player to input their move
    ├── is_game_over() -> Determines if the game is over or not
    └── play() -> Controls the game flow and logic
"""


class Board:
    def __init__(self, size=3, player_1_symbol="O", player_2_symbol="X"):
        self.size = size
        self.player_1_symbol = player_1_symbol
        self.player_2_symbol = player_2_symbol
        self.board = [[None for _ in range(self.size)] for _ in range(self.size)]

    def is_valid_move(self, location_x: int, location_y: int) -> bool:
        if self.board[location_y][location_x] in [None, " "]:
            return True
        else:
            return False

    def make_move(self, player: int, x: int, y: int) -> bool:
        """
        Adds symbol to the board. Returns True if success, False otherwise.
        """
        if player not in [1, 2]:
            raise ValueError("Player must be 1 or 2 (integer).")
        
        is_free_space = self.is_valid_move(x, y)
        if not is_free_space:
            return False
        else:
            if player == 1:
                self.board[y][x] = self.player_1_symbol
            elif player == 2:
                self.board[y][x] = self.player_2_symbol
            else:
                self.board[y][x] = "E"  # for errors that could sneak in
            
            return True
    
    def is_full(self):
        for x in self.board:
            for cell in x:
                if cell in [None, " "]:
                    return False
        return True

    def is_winner(self, player: int) -> bool:
        # check horizontal
        has_won = False
        player_symbol = self.player_1_symbol if player == 1 else self.player_2_symbol
        board = self.board  # PyCharm doesn't like self.board for some reason in iterative sequences

        # horizontal & vertical win
        for i in range(self.size):
            horizontal_count = 0
            vertical_count = 0
            for j in range(self.size):
                if board[i][j] == player_symbol:
                    horizontal_count += 1
                if board[j][i] == player_symbol:
                    vertical_count += 1
            if self.size in [horizontal_count, vertical_count]:
                return True

        # both diagonals
        diagonal_count_1 = 0
        diagonal_count_2 = 0
        for i in range(self.size):

            if board[i][i] == player_symbol:
                diagonal_count_1 += 1
            if board[self.size - (1 + i)][i] == player_symbol:
                diagonal_count_2 += 1
        if self.size in [diagonal_count_1, diagonal_count_2]:
            return True

        return False

    def display(self):
        game_board = self.board
        for i in range(len(game_board)):
            for j in range(len(game_board[i])):
                if game_board[i][j] is None:
                    game_board[i][j] = " "
            print(" | ".join(game_board[i]))
            if i != len(game_board) - 1:
                print("---"*len(game_board[i]))


class GameASCII:
    def __init__(self, size=3, player_1_symbol="O", player_2_symbol="X"):
        self.board = Board(size, player_1_symbol, player_2_symbol)

    def get_move(self, player: int):
        is_valid_move = False
        move_x, move_y = None, None

        while not is_valid_move:
            move_x, move_y = input("Please enter your move in the form x coordinate, y coordinate:\n>")\
                .strip(" ").strip(")").strip("(").split(",")  # Removes all "("," " and ")"
            if self.board.is_valid_move(int(move_x), int(move_y)):
                is_valid_move = True
            else:
                print(self.board.board[int(move_y)][int(move_x)])
                print("Invalid move. Please try again")

        self.board.make_move(player, int(move_x), int(move_y))

    def is_game_over(self):
        if self.board.is_full():
            return True, "Board is full: Draw!"
        elif self.board.is_winner(player=1):
            return True, "Player 1 wins!!"
        elif self.board.is_winner(player=2):
            return True, "Player 2 wins!!"
        return False, None

    def play(self):
        turn_counter = 0
        game_is_over = False
        while not game_is_over:
            current_player = turn_counter % 2 + 1
            self.get_move(current_player)
            self.board.display()
            turn_counter += 1
            game_is_over, reason_for_game_over = self.is_game_over()
        print(reason_for_game_over)


if __name__ == "__main__":
    game = GameASCII()
    game.play()