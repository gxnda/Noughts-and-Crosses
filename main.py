
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
        #Create Board
        self.board=[[[None] for i in range(self.size)] for i in range(self.size)]

    def is_valid_move(self, location_x: int, location_y: int) -> bool:
        if self.board[location_y, location_x] == None:
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
                self.board[y, x] = self.player_1_symbol
            elif player == 2:
                self.board[y, x] = self.player_2_symbol
            else:
                self.board[y, x] = "E" # for errors that could sneak in
            
            return True
    
    def is_full(self):
        for x in self.board:
            for cell in x:
                if cell == None:
                    return False
        return True

    def is_winner(self, player: int) -> bool:
        #check horizontal
        has_won = False
        player_symbol = self.player_1_symbol if player == 1 else self.player_2_symbol

        #Horizontal win
        for row in self.board:
            horizontal_count = 0
            for cell in row:
                if cell == player_symbol:
                    horizontal_count += 1
            if horizontal_count == self.size:
                has_won = True
        
        #Vertical win
        