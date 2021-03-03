# Author: Paul Herr
# Date: 3/1/21
# Description:
#     A two player korean board game similar to chess. Players are either blue or red. Blue always goes first. The board
#     is 9x10. There is a 3x3 area called the palace at the edge of each player's side. There are 7 types of pieces:
#
#     1 general that can only move one space vertically or horizontally within the palace.
#
#     2 guards that can only move one space vertically or horizontally. within the palace.
#
#     2 horses that can move one space vertically or horizontally and then one space diagonally forwards.
#     This piece cannot jump over other pieces. It cannot move in a direction if there is a piece blocking it
#
#     2 elephants that can move one space vertically or horizontally and then two spaces diagonally forwards.
#     This piece cannot jump over other pieces. It cannot move in a direction if there is a piece blocking it
#
#     2 chariots that can move an the length of the board vertically or horizontally. The chariot can also move along
#     the diagonal lines when in the palace.
#
#     2 cannons that can only move vertically or horizontally if there is a piece in the same row/column that it can
#     jump over. It can move any distance provided the previous requirement is met. It cannot capture other cannon
#     pieces. It cannot jump over two pieces. The cannon can also move along the diagonal lines when in the palace.
#
#     5 soldiers that can move one space forward or one space horizontally. It cannot go backwards.
#
#     Each player has a set of these pieces.
#
#     The player must checkmate the opposing general in order to win.


class JangiGame:
    """
    A two player korean board game similar to chess. Players are either blue or red. Blue always goes first. The board
    is 9x10. There is a 3x3 area called the palace at the edge of each player's side. There are 7 types of pieces:

    1 general that can only move one space vertically or horizontally within the palace.

    2 guards that can only move one space vertically or horizontally. within the palace.

    2 horses that can move one space vertically or horizontally and then one space diagonally forwards.
    This piece cannot jump over other pieces. It cannot move in a direction if there is a piece blocking it

    2 elephants that can move one space vertically or horizontally and then two spaces diagonally forwards.
    This piece cannot jump over other pieces. It cannot move in a direction if there is a piece blocking it

    2 chariots that can move an the length of the board vertically or horizontally. The chariot can also move along
    the diagonal lines when in the palace.

    2 cannons that can only move vertically or horizontally if there is a piece in the same row/column that it can
    jump over. It can move any distance provided the previous requirement is met. It cannot capture other cannon pieces.
    It cannot jump over two pieces. The cannon can also move along the diagonal lines when in the palace.

    5 soldiers that can move one space forward or one space horizontally. It cannot go backwards.

    Each player has a set of these pieces.

    The player must checkmate the opposing general in order to win.
    """

    def __init__(self):
        """
        Sets up the beginning of the game. Initializes the game state to unfinished. Set it to be the blue player's
        turn. Lastly, initializes the board and pieces to their beginning positions.
        """

        self._game_state = "UNFINISHED"
        self._blues_turn = True

        self._game_board = [
            [Chariot("red", "a1"), Elephant("red", "b1"), Horse("red", "c1"), "RGuard", None,
             "RGuard", Elephant("red", "g1"), Horse("red", "h1"), Chariot("red", "i1")],
            [None, None, None, None, General("red", "e2"),
             None, None, None, None],
            [None, Cannon("red", "b3"), None, None, None,
             None, None, Cannon("red", "h3"), None],
            [Soldier("red", "a4"), None, Soldier("red", "c4"), None, Soldier("red", "e4"),
             None, Soldier("red", "g4"), None, Soldier("red", "i4")],
            [None, None, None, None, None,
             None, None, None, None],
            [None, None, None, None, None,
             None, None, None, None],
            [Soldier("blue", "a7"), None, Soldier("blue", "c7"), None, Soldier("blue", "e7"),
             None, Soldier("blue", "g7"), None, Soldier("blue", "i7")],
            [None, Cannon("blue", "b8"), None, None, None,
             None, None, Cannon("blue", "h8"), None],
            [None, None, None, None, General("blue", "e9"),
             None, None, None, None],
            [Chariot("blue", "a10"), Elephant("blue", "b10"), Horse("blue", "c10"), "BGuard", None,
             "BGuard", Elephant("blue", "g10"), Horse("blue", "i10"), Chariot("blue", "i10")],

        ]
        #
        # self._game_board2 = {
        #     "a1": "RChariot", "b1": "RElephant", "c1": "RHorse", "d1": "RGuard", "e1": None,
        #     "f1": "RGuard", "g1": "RElephant", "h1": "RHorse", "i1": "RChariot",
        #
        #     "a2": None, "b2": None, "c2": None, "d2": None, "e2": "RGeneral",
        #     "f2": None, "g2": None, "h2": None, "i2": None,
        #
        #     "a3": None, "b3": "RCannon", "c3": None, "d3": None, "e3": None,
        #     "f3": None, "g3": None, "h3": "RCannon", "i3": None,
        #
        #     "a4": "RSoldier", "b4": None, "c4": "RSoldier", "d4": None, "e4": "RSoldier",
        #     "f4": None, "g4": "RSoldier", "h4": None, "i4": "RSoldier",
        #
        #     "a5": None, "b5": None, "c5": None, "d5": None, "e5": None,
        #     "f5": None, "g5": None, "h5": None, "i5": None,
        #
        #     "a6": None, "b6": None, "c6": None, "d6": None, "e6": None,
        #     "f6": None, "g6": None, "h6": None, "i6": None,
        #
        #     "a7": "BSoldier", "b7": None, "c7": "BSoldier", "d7": None, "e7": "BSoldier",
        #     "f7": None, "g7": "BSoldier", "h7": None, "i7": "BSoldier",
        #
        #     "a8": None, "b8": "BCannon", "c8": None, "d8": None, "e8": None,
        #     "f8": None, "g8": None, "h8": "BCannon", "i8": None,
        #
        #     "a9": None, "b9": None, "c9": None, "d9": None, "e9": "BGeneral",
        #     "f9": None, "g9": None, "h9": None, "i9": None,
        #
        #     "a10": "BChariot", "b10": "BElephant", "c10": "BHorse", "d10": "BGuard", "e10": None,
        #     "f10": "BGuard", "g10": "BElephant", "h10": "BHorse", "i10": "BChariot"
        # }
        pass

    def get_game_board(self):
        """
        Returns the game board.
        """

        return self._game_board

    def get_game_state(self):
        """
        Returns the game state.
        """

        return self._game_state

    def make_move(self, piece_location, new_location):
        """
        Attempts to move the piece specified to a new location on the board. Returns True if the move is successful.
        Returns False if the move is unsuccessful or if the game is finished.
        """

        pass

    def is_in_check(self, player_color):
        """
        Returns True if the player's general is in check.
        """

        pass


class JanggiPiece:
    """
    A Jangi piece belonging a player and it has position on the board.
    """

    def __init__(self, player, position):
        """
        Creates a Jangi piece belonging to a player's color and initialize its position on the board.
        """

        self._player = player
        self._position = position

    def get_player(self):
        """
        Return the player who owns this piece.
        """

        return self._player

    def get_position(self):
        """
        Returns the position of the piece.
        """

        return self._position

    def set_position(self, position):
        """
        Sets the position of the piece to a new location.
        """

        self._position = position

    def alphabetic_to_index(self, algebraic_notation):
        """
        Converts the alphabetic part of the algebraic notation into its corresponding index.
        """

        alpha_dict = {
            "a": 0, "b": 1, "c": 2,
            "d": 3, "e": 4, "f": 5,
            "g": 6, "h": 7, "i": 8
        }

        return alpha_dict.get(algebraic_notation[0])

    def numeric_to_index(self, algebraic_notation):
        """
        Converts the numeric part of the algebraic notation to its corresponding index.
        """

        num_dict = {
            "1": 0, "2": 1, "3": 2,
            "4": 3, "5": 4, "6": 5,
            "7": 6, "8": 7, "9": 8, "10": 9
        }

        return num_dict.get(algebraic_notation[1])

    def index_to_alphabetic(self, index):
        """
        Converts the index into the alphabetic part of the algebraic notation.
        """

        alpha_dict = {
            0: "a", 1: "b", 2: "c",
            3: "d", 4: "e", 5: "f",
            6: "g", 7: "h", 8: "i"
        }

        return alpha_dict.get(index)

    def index_to_numeric(self, index):
        """
        Converts the index into the numeric part of the algebraic notation
        """

        num_dict = {
            0: "1", 1: "2", 2: "3",
            3: "4", 4: "5", 5: "6",
            6: "7", 7: "8", 8: "9", 9: "10"
        }

        return num_dict.get(index)

    def algebraic_notation_convertor(self, algebraic_notation):
        """
        Converts algebraic notation to index notation. Returns a tuple containing the two values.
        """

        return [self.alphabetic_to_index(algebraic_notation), self.numeric_to_index(algebraic_notation)]

    def indices_to_algebraic_notation(self, x_index, y_index):
        """
        Converts the indices to algebraic notation.
        """

        return self.index_to_alphabetic(x_index) + self.index_to_numeric(y_index)


class Soldier(JanggiPiece):
    """
    A soldier piece that can move one space forward or one space horizontally. It cannot go backwards.
    """

    def __init__(self, player, position):
        """
        Initializes a soldier piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)
        self._piece_name = "soldier"

    def valid_movements(self, game_board=None):
        """
        Returns a set of valid movements for the piece.
        """

        valid_movements_set = set()
        column = self.alphabetic_to_index(self.get_position())
        row = self.numeric_to_index(self.get_position())

        # Both players are able to move left or right, unless they are at the edge of the board.
        if column != 0 and column != 8:
            valid_movements_set.add(self.indices_to_algebraic_notation(column + 1, row))
            valid_movements_set.add(self.indices_to_algebraic_notation(column - 1, row))
        elif column == 0:
            valid_movements_set.add(self.indices_to_algebraic_notation(column + 1, row))
        else:
            valid_movements_set.add(self.indices_to_algebraic_notation(column - 1, row))

        # Red can only move to a higher index (down the board), while blue can only move to a lower index (up the board)
        if self.get_player() == "red":
            if row != 9:
                valid_movements_set.add(self.indices_to_algebraic_notation(column, row + 1))
        else:
            if row != 0:
                valid_movements_set.add(self.indices_to_algebraic_notation(column, row - 1))

        return valid_movements_set

    pass


class Guard(JanggiPiece):
    """
    A guard piece that can move one space vertically or horizontally. It is only able to move within the palace.
    """

    def __init__(self, player, position):
        """
        Initializes a guard piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)
        self._piece_name = "guard"

    def valid_movements(self, game_board=None):
        """
        Returns a set of valid movements for the piece.
        """
        valid_movements_set = set()
        column = self.alphabetic_to_index(self.get_position())
        row = self.numeric_to_index(self.get_position())

        if self.get_player() == "red":

            # Allows horizontal movement within the red palace only.
            if column != 3 and column != 5:
                valid_movements_set.add(self.indices_to_algebraic_notation(column + 1, row))
                valid_movements_set.add(self.indices_to_algebraic_notation(column - 1, row))
            elif column == 3:
                valid_movements_set.add(self.indices_to_algebraic_notation(column + 1, row))
            elif column == 5:
                valid_movements_set.add(self.indices_to_algebraic_notation(column - 1, row))

            # Allows vertical movement within the red palace only.
            if row != 0 or row != 2:
                valid_movements_set.add(self.indices_to_algebraic_notation(column, row + 1))
                valid_movements_set.add(self.indices_to_algebraic_notation(column, row - 1))
            elif row == 0:
                valid_movements_set.add(self.indices_to_algebraic_notation(column, row + 1))
            elif row == 2:
                valid_movements_set.add(self.indices_to_algebraic_notation(column, row - 1))

        else:

            # Allows horizontal movement within the blue palace only.
            if column != 3 and column != 5:
                valid_movements_set.add(self.indices_to_algebraic_notation(column + 1, row))
                valid_movements_set.add(self.indices_to_algebraic_notation(column - 1, row))
            elif column == 3:
                valid_movements_set.add(self.indices_to_algebraic_notation(column + 1, row))
            elif column == 5:
                valid_movements_set.add(self.indices_to_algebraic_notation(column - 1, row))

            # Allows vertical movement within the blue palace only.
            if row != 7 or row != 9:
                valid_movements_set.add(self.indices_to_algebraic_notation(column, row + 1))
                valid_movements_set.add(self.indices_to_algebraic_notation(column, row - 1))
            elif row == 9:
                valid_movements_set.add(self.indices_to_algebraic_notation(column, row + 1))
            elif row == 7:
                valid_movements_set.add(self.indices_to_algebraic_notation(column, row - 1))

        return valid_movements_set


class General(Guard):
    """
    A general piece that can move one space vertically or horizontally. It is only able to move within the palace.
    The player loses if his general is checkmated.
    """

    def __init__(self, player, position):
        """
        Initializes a general piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)
        self._piece_name = "general"

    pass


class Horse(JanggiPiece):
    """
    A horse piece that can move one space vertically or horizontally and then one space diagonally forwards.
    This piece cannot jump over other pieces. It cannot move in a direction if there is a piece blocking it.
    """

    def __init__(self, player, position):
        """
        Initializes a horse piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)
        self._piece_name = "horse"

    def valid_movements(self, game_board=None):
        """
        Returns a set of valid movements for the piece.
        """
        valid_movements_set = set()
        column = self.alphabetic_to_index(self.get_position())
        row = self.numeric_to_index(self.get_position())

        # First scenario: moving to to a higher index of the rows (down the board).
        # Make sure we aren't at bottom edge and that the space below the piece is unoccupied.
        if row + 2 <= 9 and game_board[row + 1][column] is None:

            # Checks for the left and right edges.
            # Also makes sure the space the piece moves into is unoccupied by the current player's pieces.
            if 0 < column < 8:
                if game_board[row + 2][column + 1].get_player() != self.get_player():
                    valid_movements_set.add(self.indices_to_algebraic_notation(column + 1, row + 2))

                if game_board[row + 2][column - 1].get_player() != self.get_player():
                    valid_movements_set.add(self.indices_to_algebraic_notation(column - 1, row + 2))

            elif column == 0:
                if game_board[row + 2][column + 1].get_player() != self.get_player():
                    valid_movements_set.add(self.indices_to_algebraic_notation(column + 1, row + 2))

            elif column == 8:
                if game_board[row + 2][column - 1].get_player() != self.get_player():
                    valid_movements_set.add(self.indices_to_algebraic_notation(column - 1, row + 2))

        # Second scenario: moving to to a lower index of the rows (up the board).
        # Make sure we aren't at top edge and that the space above the piece is unoccupied.
        if row - 2 >= 0 and game_board[row - 1][column] is None:

            # Checks for the left and right edges.
            # Also makes sure the space the piece moves into is unoccupied by the current player's pieces.
            if 0 < column < 8:
                if game_board[row - 2][column + 1].get_player() != self.get_player():
                    valid_movements_set.add(self.indices_to_algebraic_notation(column + 1, row - 2))

                if game_board[row - 2][column - 1].get_player() != self.get_player():
                    valid_movements_set.add(self.indices_to_algebraic_notation(column - 1, row - 2))

            elif column == 0:
                if game_board[row + 2][column + 1].get_player() != self.get_player():
                    valid_movements_set.add(self.indices_to_algebraic_notation(column + 1, row - 2))

            elif column == 9:
                if game_board[row + 2][column - 1].get_player() != self.get_player():
                    valid_movements_set.add(self.indices_to_algebraic_notation(column - 1, row - 2))

        # Third scenario: moving to a higher index of the columns (to the right).
        # Make sure we aren't at the right edge and the space to the right of the piece is unoccupied.
        if column + 2 <= 8 and game_board[row][column + 1] is None:

            # Check for top and bottom edges.
            # Also makes sure the space the piece moves into is unoccupied by the current player's pieces.
            if 0 < row < 9:
                if game_board[row + 1][column + 2].get_player() != self.get_player():
                    valid_movements_set.add(self.indices_to_algebraic_notation(column + 2, row + 1))

                if game_board[row - 1][column + 2].get_player() != self.get_player():
                    valid_movements_set.add(self.indices_to_algebraic_notation(column + 2, row - 1))

            elif row == 0:
                if game_board[row + 1][column + 2].get_player() != self.get_player():
                    valid_movements_set.add(self.indices_to_algebraic_notation(column + 2, row + 1))

            elif row == 9:
                if game_board[row - 1][column + 2].get_player() != self.get_player():
                    valid_movements_set.add(self.indices_to_algebraic_notation(column + 2, row - 1))

        # Fourth scenario: moving to a lower index of the columns (to the left).
        # Make sure we aren't at the left edge and the space to the left of the piece is unoccupied.
        if column - 2 >= 0 and game_board[row][column - 1] is None:

            # Check for top and bottom edges.
            # Also makes sure the space the piece moves into is unoccupied by the current player's pieces.
            if 0 < row < 9:
                if game_board[row + 1][column - 2].get_player() != self.get_player():
                    valid_movements_set.add(self.indices_to_algebraic_notation(column - 2, row + 1))

                if game_board[row - 1][column - 2].get_player() != self.get_player():
                    valid_movements_set.add(self.indices_to_algebraic_notation(column - 2, row - 1))

            elif row == 0:
                if game_board[row + 1][column - 2].get_player() != self.get_player():
                    valid_movements_set.add(self.indices_to_algebraic_notation(column - 2, row + 1))

            elif row == 9:
                if game_board[row - 1][column - 2].get_player() != self.get_player():
                    valid_movements_set.add(self.indices_to_algebraic_notation(column - 2, row - 1))

        return valid_movements_set


class Elephant(Horse):
    """
    An elephant piece that can move one space vertically or horizontally and then two spaces diagonally forward.
    This piece cannot jump over other pieces. It cannot move in a direction if there is a piece blocking it.
    """

    def __init__(self, player, position):
        """
        Initializes an elephant piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)
        self._piece_name = "elephant"

    def valid_movements(self, game_board=None):
        """
        Returns a set of valid movements for the piece.
        """
        horse_movements_set = super().valid_movements(game_board)

        for position in horse_movements_set:
            if position is not None:
                horse_movements_set.remove(position)


class Chariot(JangiGame):
    """
    A chariot piece that can move an the length of the board vertically or horizontally. The chariot can also move along
    the diagonal lines when in the palace.
    """

    def __init__(self, player, position):
        """
        Initializes a chariot piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)
        self._piece_name = "chariot"

    def valid_movements(self, game_board=None):
        """
        Returns a set of valid movements for the piece.
        """
        valid_movements_set = set()
        column = self.alphabetic_to_index(self.get_position())
        row = self.numeric_to_index(self.get_position())

    pass


class Cannon(Chariot):
    """
    A cannon piece that can only move vertically or horizontally if there is a piece in the same row/column that it can
    jump over. It can move any distance provided the previous requirement is met. It cannot capture other cannon pieces.
    It cannot jump over two pieces. The cannon can also move along the diagonal lines when in the palace.
    """

    def __init__(self, player, position):
        """
        Initializes a cannon piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)
        self._piece_name = "cannon"

    def valid_movements(self, game_board=None):
        """
        Returns a set of valid movements for the piece.
        """
        valid_movements_set = set()
        column = self.alphabetic_to_index(self.get_position())
        row = self.numeric_to_index(self.get_position())

    pass
