# Author: Paul Herr
# Date: 3/1/21
# Description:
#     A two player korean board game similar to chess. Players are either blue or red. Blue always goes first. The board
#     is 9x10. There is a 3x3 area called the palace at the edge of each player's side. There are 7 types of pieces:
#
#     1 general that can only move one space vertically or horizontally within the palace.
#
#     2 guards that can only move one space vertically or horizontally within the palace.
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


# -------------------------------DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS-------------------------------
#
#   (1) Initializing the board and (2) Determining how to represent pieces at the given location on the board:
#
#           Currently, I plan on using a list to store the locations of the pieces on the board. The list is composed of
#       10 elements which are also lists, and they represents the rows of the board. Each of the 10 lists contain 9
#       elements, which will represent the columns of the board. I will hard code the starting positions into the list,
#       since we don't have to account for the option to switch the horse and elephant around. For each space that does
#       not have a piece, it will be initialized to None.
#
#       At the moment, I also have a dictionary representation of the board commented out. Depending on how the rest of
#       my functions go, I could switch to a dictionary representation of the board in case it's easier to implement,
#       but for now I am planning on using the list representation. The dictionary representation will have the keys be
#       the algebraic notation for each space on the board. Similar to the list representation, I will hard code the
#       starting positions to its corresponding keys. If a space does not have a piece, the key value will be to None.
#
#       Lastly, when a JanggiPiece is created, it is initialized to belonging to a player and having a position on the
#       board. This is how I will keep track of which piece belongs to which player and their current locations. The
#       position will be stored in algebraic notation as a string.
#
#   (3) Determining how to validate a given move according to the rules for each piece, turn taking, and other game
#       rules:
#
#           I will have each different type of piece as its own class. Each piece will inherit from JanggiPiece. Each
#       piece type will also have a variable to store their piece type. Each class will have their own valid_movements
#       method. This method will check for all possible positions that the piece is able to move to and ensure that it
#       is a valid move; this will be expanded upon below.
#
#       I will have multiple helper functions to convert algebraic notation to its list indices. First will be a
#       function to convert the alphabetic part of the notation by using a dictionary: "a" will correspond to 0, "b"
#       will correspond to 1, and so on. The second function will convert the numerical part of the notation: "1" will
#       correspond to 0, "2" will correspond to 1, and so on. I will have another two functions to convert the indices
#       back to algebraic notation, using the same method above. The column index would correspond to the alphabetical
#       part of the notation, while the row index will be the numerical part.
#
#       The Soldier class is only able to move forward and horizontally. To do so, I will check for the current position
#       of the soldier piece and convert it to its index notation. Using an if statement, if the soldier piece is on the
#       left or right edge, it is only allowed to move to the opposite direction by adding or subtracting 1 from the
#       column index. Otherwise, it can move left or right by adding or subtracting the column index. Using a different
#       if statement, I will check for the ownership of the piece using a getter. If it is the red player, it will only
#       be allowed to move down, while blue will only be allowed to move up by adding 1 to the row index and vice versa
#       for the blue player. Nested within the if statements above, if the location the piece will move to has another
#       piece that the current player owns, then it is not a valid movement. If the movements are valid, then it will
#       convert the indices back into algebraic notation using the helper functions above and add the location as a
#       valid movement in the set called valid_movements_set.
#
#       The Guard class is only able to move one space in any direction in their respective palaces. Implementation will
#       be similar to the Soldier class.
#       - First check which player owns the piece.
#       - Next check for the position of the Guard piece to be moved and convert the algebraic notation to indices.
#       - Using an if statement, change the indices for the movement limitations based on the player.
#       - Using list indices, do not allow the pieces to move past the edges of the palace.
#       - Add or subtract 1 to the row index, column index, or both indices for vertical, horizontal, or diagonal
#         movement respectively.
#       - Check the location if there is a piece owned by the player already there.
#       - If not, then convert the indices back into algebraic notation and add it to the set valid_movements_set.
#       - Return valid_movements_set
#
#       The General class will also inherit from the Guard class, since their movements are the same. Additionally, the
#       General cannot put itself in check.
#       - Call the original guard method and save the set received into valid_movements_set.
#       - Iterate through the game board. If the piece belongs to the opponent, call their valid moves method.
#       - While in the loop, iterate through the General's valid_movements_set.
#       - If the location in the General's valid_movements_set is in the opponent's piece's valid moves set, then remove
#         it from the General's valid_movements_set.
#       - Return valid_movements_set
#
#       The Horse class is allowed to move one space vertical or horizontally, and then one space diagonally forwards.
#       - First check the position of the Horse piece to be moved and convert the algebraic notation to indices.
#       - Next add/subtract 1 from the indices and check if there is a piece already in the location adjacent to the
#         horse piece.
#       - There are 4 if statements for each direction: up, down, left, right.
#       - If the location is not None, skip this part of the if statement, since horses are not able to jump over
#         pieces.
#       - Otherwise, check for the diagonal movements by manipulating the list indices again.
#       - There should be another two if statements for each direction: up and to the right, up and to the left, left
#         and up, left, and down, and so forth.
#       - If the location is None or contains an enemy piece, then convert the indices to algebraic notation and add it
#         to the set valid_movements_set.
#       - Return valid_movements_set
#
#       The Elephant class will also inherit from the Horse class, since their movements are the similar. The only
#       difference is that the Elephant class can also move one extra space diagonally.
#       - Call the original horse method and save the set received from there into horse_movements_set.
#       - Iterate through horse_movements_set.
#       - For each iteration, convert the location to its indices.
#       - Check the index; if the index is not None, then remove it from the set.
#       - Find the position of the elephant piece to be moved.
#       - Add 1 or 2 from the column or row indices to determine which directions to move to match the positions in
#         horse_movements_set.
#       - Check the next diagonal by adding/subtracting 1 to the row and column indices.
#       - If the next diagonal is None or has an enemy piece, then add it to the set valid_movements_set.
#       - Return valid_movements_set
#
#       The Chariot class can move in any the length of the board vertically and horizontally.
#       - Find the position of the chariot piece to be moved and convert it to indices.
#       - Starting from the chariot piece, iterate backwards through the column index until we reach a piece or the
#         edge.
#       - For each space that is None, add it to the valid_movements_set.
#       - If the piece is an enemy piece or the edge, add the enemy location or edge as the last valid movement and stop
#         iterating through that side.
#       - If the piece is a friendly piece, add the index to one higher/lower than the friendly piece as the last valid
#         movement on that side and stop iterating.
#       - Next, iterate forwards through the columns index and do the same thing above.
#       - Next, iterate through the row indices to go above and below the chariot piece. Do the same thing above.
#       - If the chariot is in the palace, check the diagonals within the palaces by manipulating the row and column
#         indices in a similar way to the horse/elephant pieces.
#       - Return valid_movements_set
#
#       The Cannon class can only move if there is a piece it can hop over. It will also inherit from the Chariot class,
#       since their movements is similar in that they are able to move vertically and horizontally the length of the
#       board as long. The Cannon class only requires extra functionality to continue iterating past the first piece it
#       encounters.
#       - Call the original chariot method and save the set received into chariot_movements_set.
#       - Iterate through the set and convert the algebraic notation to indices.
#       - If the location specified is None, then remove it from the set. This gives us the set of all locations with a
#         piece that the cannon can jump over.
#       - Check the locations of the pieces in the set to see which direction they are in compared to the cannon.
#       - Starting from the pieces in the set, iterate away from the cannon until we reach another piece.
#       - If the piece is an enemy piece or the edge, add the enemy location or edge as the last valid movement and stop
#         iterating through that side.
#       - If the piece is a friendly piece, add the index to one higher/lower than the friendly piece as the last valid
#         movement on that side and stop iterating.
#       - At most, do this 4 times if there is a piece in all four directions of the cannon.
#       - Return valid_movements_set
#
#      (4), (5), (6), and (7)
#
#       With the above, each piece should be able to return a set of valid moves. This set will be used in the method
#       is_in_check.
#       - This method will take a player's color as a parameter to check if that player is in check.
#       - Get the current player's general's location.
#       - Iterate through the game board and if the piece belongs to the opposite player, call its valid_moves method.
#       - If the player's general's location is in any of the opponent's pieces valid_movements_set return True.
#
#       The player's turns will be kept track of by a truth value. True for blue's turn, False for red's.
#
#       In the make_move method:
#       - This takes two parameters in algebraic notation: the piece_location, and the new_location it will be moved to.
#       - First call the is_in_check method for the current player.
#       - If it's true, iterate through the current player's palace indices to search for the general's location.
#       - Get the general's location.
#       - If piece_location is not the same as the general's location, then return False.
#       - If the current player's general is not in check, then call the get_player method to make sure that it is the
#         current player's piece.
#       - If it is the current player's piece, then call the valid_moves method for the piece.
#       - If new_location is not in the valid_movements_set for that piece, return False.
#       - Otherwise, set the piece's position to new_location.
#       - Convert new_location to its indices and replace whatever on the game board at the indices location with the
#         moving piece.
#       - Lastly, iterate through the opponent's palace.
#       - When the opponent's general is reached, call its valid_moves method.
#       - If the opponent's general's valid_movements_set is empty, then the current player wins.
#       - If the current player wins, change the game state to reflect so.
#       - Regardless, change the player's turns truth value to its opposite to change turns.
#       - Return True if the move was successful.
#
# -----------------------------DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS END-----------------------------


class JanggiGame:
    """
    A two player korean board game similar to chess. Players are either blue or red. Blue always goes first. The board
    is 9x10. There is a 3x3 area called the palace at the edge of each player's side. There are 7 types of pieces:

    1 general that can only move one space vertically or horizontally within the palace.

    2 guards that can only move one space vertically or horizontally within the palace.

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
            [Chariot("red", "a1"), Elephant("red", "b1"), Horse("red", "c1"),
             Guard("red", "d1"), None, Guard("red", "f1"),
             Elephant("red", "g1"), Horse("red", "h1"), Chariot("red", "i1")],

            # # No guards
            # [Chariot("red", "a1"), Elephant("red", "b1"), Horse("red", "c1"),
            #  None, None, None,
            #  Elephant("red", "g1"), Horse("red", "h1"), Chariot("red", "i1")],

            [None, None, None,
             None, General("red", "e2"), None,
             None, None, None],

            # # No general
            # [None, None, None,
            #  None, None, None,
            #  None, None, None],

            [None, Cannon("red", "b3"), None,
             None, None, None,
             None, Cannon("red", "h3"), None],

            [Soldier("red", "a4"), None, Soldier("red", "c4"),
             None, Soldier("red", "e4"), None,
             Soldier("red", "g4"), None, Soldier("red", "i4")],

            [None, None, None,
             None, None, None,
             None, None, None],

            [None, None, None,
             None, None, None,
             None, None, None],

            [Soldier("blue", "a7"), None, Soldier("blue", "c7"),
             None, Soldier("blue", "e7"), None,
             Soldier("blue", "g7"), None, Soldier("blue", "i7")],

            [None, Cannon("blue", "b8"), None,
             None, None, None,
             None, Cannon("blue", "h8"), None],

            [None, None, None,
             None, General("blue", "e9"), None,
             None, None, None],

            # # No general
            # [None, None, None,
            #  None, None, None,
            #  None, None, None],

            [Chariot("blue", "a10"), Elephant("blue", "b10"), Horse("blue", "c10"),
             Guard("blue", "d10"), None, Guard("blue", "f10"),
             Elephant("blue", "g10"), Horse("blue", "h10"), Chariot("blue", "i10")]

            # # No guards
            # [Chariot("blue", "a10"), Elephant("blue", "b10"), Horse("blue", "c10"),
            #  None, None, None,
            #  Elephant("blue", "g10"), Horse("blue", "h10"), Chariot("blue", "i10")]
        ]

        self._remaining_blue_pieces = []
        self._remaining_red_pieces = []

        # self._dict_game_board = {
        #     "a1": Chariot("red", "a1"), "b1": Elephant("red", "b1"), "c1": Horse("red", "c1"),
        #     "d1": Guard("red", "d1"), "e1": None, "f1": Guard("red", "f1"),
        #     "g1": Elephant("red", "g1"), "h1": Horse("red", "h1"), "i1": Chariot("red", "i1"),
        #
        #     "a2": None, "b2": None, "c2": None,
        #     "d2": None, "e2": General("red", "e2"), "f2": None,
        #     "g2": None, "h2": None, "i2": None,
        #
        #     "a3": None, "b3": Cannon("red", "b3"), "c3": None,
        #     "d3": None, "e3": None, "f3": None,
        #     "g3": None, "h3": Cannon("red", "h3"), "i3": None,
        #
        #     "a4": Soldier("red", "a4"), "b4": None, "c4": Soldier("red", "c4"),
        #     "d4": None, "e4": Soldier("red", "e4"), "f4": None,
        #     "g4": Soldier("red", "g4"), "h4": None, "i4": Soldier("red", "i4"),
        #
        #     "a5": None, "b5": None, "c5": None,
        #     "d5": None, "e5": None, "f5": None,
        #     "g5": None, "h5": None, "i5": None,
        #
        #     "a6": None, "b6": None, "c6": None,
        #     "d6": None, "e6": None, "f6": None,
        #     "g6": None, "h6": None, "i6": None,
        #
        #     "a7": Soldier("blue", "a7"), "b7": None, "c7": Soldier("blue", "c7"),
        #     "d7": None, "e7": Soldier("blue", "e7"), "f7": None,
        #     "g7": Soldier("blue", "g7"), "h7": None, "i7": Soldier("blue", "i7"),
        #
        #     "a8": None, "b8": Cannon("blue", "b8"), "c8": None,
        #     "d8": None, "e8": None, "f8": None,
        #     "g8": None, "h8": Cannon("blue", "h8"), "i8": None,
        #
        #     "a9": None, "b9": None, "c9": None,
        #     "d9": None, "e9": General("blue", "e9"), "f9": None,
        #     "g9": None, "h9": None, "i9": None,
        #
        #     "a10": Chariot("blue", "a10"), "b10": Elephant("blue", "b10"), "c10": Horse("blue", "c10"),
        #     "d10": Guard("blue", "d10"), "e10": None, "f10": Guard("blue", "f10"),
        #     "g10": Elephant("blue", "g10"), "h10": Horse("blue", "h10"), "i10": Chariot("blue", "i10")
        # }

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
        Attempts to move the piece specified to a new location on the board. A player is not allowed to leave their
        general in check. A player can skip their turn by making specifying the new location as the same as their piece
        location.

        Function requires the location of the piece to be moved and the location of where to move the piece.

        Returns True if the move is successful. Returns False if the move is unsuccessful or if the game is
        finished.
        """

        print("Attempting: ", piece_location, "->", new_location)
        dummy_piece = JanggiPiece(None, None)       # Used to use the class methods.
        piece_row = dummy_piece.numeric_to_index(piece_location)
        piece_column = dummy_piece.alphabetic_to_index(piece_location)
        new_row = dummy_piece.numeric_to_index(new_location)
        new_column = dummy_piece.alphabetic_to_index(new_location)
        piece_to_be_moved = self._game_board[piece_row][piece_column]
        location_to_move_to = self._game_board[new_row][new_column]

        # Return False if there is no piece in the location.
        if piece_to_be_moved is None:
            print(1)
            return False

        # Return False if it's not the current player's piece.
        if self._blues_turn:
            if piece_to_be_moved.get_player() != "blue":
                print(2)
                return False

        if not self._blues_turn:
            if piece_to_be_moved.get_player() != "red":
                print(3)
                return False

        # The user passes their turn only available if they're not in check.
        if self._blues_turn:
            if not self.is_in_check("blue"):
                if piece_location == new_location:
                    self._blues_turn = not self._blues_turn
                    return True

        elif not self._blues_turn:
            if not self.is_in_check("red"):
                if piece_location == new_location:
                    self._blues_turn = not self._blues_turn
                    return True

        # Return False if the movement is invalid.
        if new_location not in piece_to_be_moved.valid_movements(self._game_board):
            print(4)
            return False

        # Move the piece into the new position, and remove the piece from the old position. Update its position.
        self._game_board[new_row][new_column] = piece_to_be_moved
        self._game_board[piece_row][piece_column] = None
        self._game_board[new_row][new_column].set_position(piece_to_be_moved.indices_to_algebraic_notation(new_column, new_row))

        print(self._game_board[new_row][new_column])

        # Return False if the move will make the player be in check. Reset the board back to its previous state if so.
        if self._blues_turn:
            if self.is_in_check("blue"):
                print(5)
                self._game_board[piece_row][piece_column] = piece_to_be_moved
                self._game_board[new_row][new_column] = location_to_move_to
                return False
        else:
            if self.is_in_check("red"):
                print(6)
                self._game_board[piece_row][piece_column] = piece_to_be_moved
                self._game_board[new_row][new_column] = location_to_move_to
                return False

        self._blues_turn = not self._blues_turn

        return True

    def is_in_check(self, player_color):
        """
        Checks for all possible moves for the opponent's pieces. The current player's general is in check if the their
        general's location is a valid move for any of the opponent's pieces.

        Returns True if the player's general is in check.
        """

        opponent_movements_set = set()
        general_location = None

        for row in self._game_board:
            for column in row:

                if column is not None:
                    if column.get_player() != player_color:
                        opponent_movements_set.update(column.valid_movements(self._game_board))

                    else:
                        if column.get_piece_name() == "general":
                            general_location = column.get_position()

        if general_location in opponent_movements_set:
            return True

        return False


class JanggiPiece:
    """
    A Janggi piece belonging a player and it has position on the board.

    All pieces will inherit from JanggiPiece, since all pieces need to belong to a player and be at a position.
    """

    def __init__(self, player, position):
        """
        Creates a Janggi piece belonging to a player's color and initialize its position on the board.
        """

        self._player = player
        self._position = position
        self._piece_type = "Generic Janggi Piece"

    def get_player(self):
        """
        Returns the player who owns this piece.
        """

        return self._player

    def get_piece_name(self):
        """
        Returns the name of the piece.
        """

        return self._piece_type

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
        Converts the alphabetic part of the algebraic notation to its index notation for columns.

        Takes an algebraic notation from a1 to i10.
        Returns the index of the alphabetical part.
        """

        alpha_dict = {
            "a": 0, "b": 1, "c": 2,
            "d": 3, "e": 4, "f": 5,
            "g": 6, "h": 7, "i": 8
        }

        return alpha_dict.get(algebraic_notation[0])

    def numeric_to_index(self, algebraic_notation):
        """
        Converts the numeric part of the algebraic notation to its index notation for rows.

        Takes an algebraic notation from a1 to i10.
        Returns the index of the numerical part.
        """

        algebraic_notation.lower()

        num_dict = {
            "1": 0, "2": 1, "3": 2,
            "4": 3, "5": 4, "6": 5,
            "7": 6, "8": 7, "9": 8, "10": 9
        }

        return num_dict.get(algebraic_notation[1:])

    def index_to_alphabetic(self, index):
        """
        Converts the index for columns to the alphabetical part of the algebraic notation.

        Takes an index from 0 to 8.
        Returns the string of the letter corresponding to the alphabetic part of the algebraic notation.
        """

        alpha_dict = {
            0: "a", 1: "b", 2: "c",
            3: "d", 4: "e", 5: "f",
            6: "g", 7: "h", 8: "i"
        }

        return alpha_dict.get(index)

    def index_to_numeric(self, index):
        """
        Converts the index for rows to the numeric part of the algebraic notation.

        Takes an index from 0 to 9.
        Returns the string of the number corresponding to the numeric part of the algebraic notation.
        """

        num_dict = {
            0: "1", 1: "2", 2: "3",
            3: "4", 4: "5", 5: "6",
            6: "7", 7: "8", 8: "9", 9: "10"
        }

        return num_dict.get(index)

    def algebraic_notation_convertor(self, algebraic_notation):
        """
        Converts algebraic notation to its index notation.

        Takes an algebraic expression from a1 to i10.
        Returns a tuple containing the index of the column and row.
        """

        return [self.alphabetic_to_index(algebraic_notation), self.numeric_to_index(algebraic_notation)]

    def indices_to_algebraic_notation(self, columns, rows):
        """
        Converts the indices to its algebraic notation.

        Takes the index for the columns and then rows.
        Returns the string of the algebraic notation.
        """

        return self.index_to_alphabetic(columns) + self.index_to_numeric(rows)

    def horizontal_movement_check(self, game_board, h_lo_bound=0, h_hi_bound=8):
        """
        Checks if the piece is able to move left or right one space.

        Takes the game board, and lower and upper boundary of the horizontal limits.
        Returns a list of positions it can move to.
        """

        # Changes the current piece's location from algebraic notation to list indices.
        column = self.alphabetic_to_index(self.get_position())
        row = self.numeric_to_index(self.get_position())
        h_movements_set = set()

        # The piece is not at the edge.
        if column != h_lo_bound and column != h_hi_bound:

            # The if statements checks to see if the square is empty.
            # If the square is not empty, check to see if the piece there is the current player's piece.
            # Add it to the list of valid moves if the square is empty or the piece is not the player's piece.

            if game_board[row][column + 1] is None:
                h_movements_set.add(self.indices_to_algebraic_notation(column + 1, row))

            elif game_board[row][column + 1].get_player() != self.get_player():
                h_movements_set.add(self.indices_to_algebraic_notation(column + 1, row))

            if game_board[row][column - 1] is None:
                h_movements_set.add(self.indices_to_algebraic_notation(column - 1, row))

            elif game_board[row][column - 1].get_player() != self.get_player():
                h_movements_set.add(self.indices_to_algebraic_notation(column - 1, row))

        # Piece is at the edge of the lower boundary.
        if column == h_lo_bound:
            if game_board[row][column + 1] is None:
                h_movements_set.add(self.indices_to_algebraic_notation(column + 1, row))

            elif game_board[row][column + 1].get_player() != self.get_player():
                h_movements_set.add(self.indices_to_algebraic_notation(column + 1, row))

        # Piece is at the edge of the upper boundary.
        if column == h_hi_bound:
            if game_board[row][column - 1] is None:
                h_movements_set.add(self.indices_to_algebraic_notation(column - 1, row))

            elif game_board[row][column - 1].get_player() != self.get_player():
                h_movements_set.add(self.indices_to_algebraic_notation(column - 1, row))

        return h_movements_set

    def vertical_movement_check(self, game_board, v_lo_bound=0, v_hi_bound=9):
        """
        Checks if the piece is able to move up or down one space.

        Takes the game board, and lower and upper boundary of the vertical limits.
        Returns a list of positions it can move to.
        """

        # Changes algebraic notation to list indices.
        column = self.alphabetic_to_index(self.get_position())
        row = self.numeric_to_index(self.get_position())
        v_movements_set = set()

        # If the piece's movement is limited to only horizontal movements.
        if row == v_lo_bound and row == v_hi_bound:
            return v_movements_set

        # The piece is not at the edge.
        if row != v_lo_bound and row != v_hi_bound:

            # The if statements checks to see if the square is empty.
            # If the square is not empty, check to see if the piece there is the current player's piece.
            # Add it to the list of valid moves if the square is empty or the piece is not the player's piece.

            if game_board[row + 1][column] is None:
                v_movements_set.add(self.indices_to_algebraic_notation(column, row + 1))

            elif game_board[row + 1][column].get_player() != self.get_player():
                v_movements_set.add(self.indices_to_algebraic_notation(column, row + 1))

            if game_board[row - 1][column] is None:
                v_movements_set.add(self.indices_to_algebraic_notation(column, row - 1))

            elif game_board[row - 1][column].get_player() != self.get_player():
                v_movements_set.add(self.indices_to_algebraic_notation(column, row - 1))

        # Piece is at the edge of the lower boundary.
        if row == v_lo_bound:
            if game_board[row + 1][column] is None:
                v_movements_set.add(self.indices_to_algebraic_notation(column, row + 1))

            elif game_board[row + 1][column].get_player() != self.get_player():
                v_movements_set.add(self.indices_to_algebraic_notation(column, row + 1))

        # Piece is at the edge of the upper boundary.
        if row == v_hi_bound:
            if game_board[row - 1][column] is None:
                v_movements_set.add(self.indices_to_algebraic_notation(column, row - 1))

            elif game_board[row - 1][column].get_player() != self.get_player():
                v_movements_set.add(self.indices_to_algebraic_notation(column, row - 1))

        return v_movements_set

    def diagonal_movement_check(self, game_board, h_lo_bound=0, h_hi_bound=8, v_lo_bound=0, v_hi_bound=9):
        """
        Checks if the piece is able to diagonally one space.

        Takes the game board, and lower and upper boundary of the horizontal and vertical limits
        Returns a list of positions it can move to.
        """

        # Changes algebraic notation to list indices.
        column = self.alphabetic_to_index(self.get_position())
        row = self.numeric_to_index(self.get_position())
        d_movements_set = set()

        # Executes if the piece is not at any of the edges.
        if v_lo_bound < row < v_hi_bound and h_lo_bound < column < h_hi_bound:

            # The if statements checks to see if the square is empty.
            # If the square is not empty, check to see if the piece there is the current player's piece.
            # Add it to the list of valid moves if the square is empty or the piece is not the player's piece.

            # Move top left
            if game_board[row - 1][column - 1] is None:
                d_movements_set.add(self.indices_to_algebraic_notation(column - 1, row - 1))

            elif game_board[row - 1][column - 1].get_player() != self.get_player():
                d_movements_set.add(self.indices_to_algebraic_notation(column - 1, row - 1))

            # Move top right
            if game_board[row - 1][column + 1] is None:
                d_movements_set.add(self.indices_to_algebraic_notation(column + 1, row - 1))

            elif game_board[row - 1][column + 1].get_player() != self.get_player():
                d_movements_set.add(self.indices_to_algebraic_notation(column + 1, row - 1))

            # Move bottom right
            if game_board[row + 1][column + 1] is None:
                d_movements_set.add(self.indices_to_algebraic_notation(column + 1, row + 1))

            elif game_board[row + 1][column + 1].get_player() != self.get_player():
                d_movements_set.add(self.indices_to_algebraic_notation(column + 1, row + 1))

            # Move bottom left
            if game_board[row + 1][column - 1] is None:
                d_movements_set.add(self.indices_to_algebraic_notation(column - 1, row + 1))

            elif game_board[row + 1][column - 1].get_player() != self.get_player():
                d_movements_set.add(self.indices_to_algebraic_notation(column - 1, row + 1))

        # If the piece is on the top edge.
        if row == v_lo_bound:

            # If the piece is not in the right corner
            if column != h_hi_bound:

                # Move bottom right
                if game_board[row + 1][column + 1] is None:
                    d_movements_set.add(self.indices_to_algebraic_notation(column + 1, row + 1))

                elif game_board[row + 1][column + 1].get_player() != self.get_player():
                    d_movements_set.add(self.indices_to_algebraic_notation(column + 1, row + 1))

            # If the piece is not in the left corner.
            if column != h_lo_bound:

                # Move bottom left
                if game_board[row + 1][column - 1] is None:
                    d_movements_set.add(self.indices_to_algebraic_notation(column - 1, row + 1))

                elif game_board[row + 1][column - 1].get_player() != self.get_player():
                    d_movements_set.add(self.indices_to_algebraic_notation(column - 1, row + 1))

        # If the piece is on the bottom edge.
        if row == v_hi_bound:

            # If the piece is not in the right corner.
            if column != h_hi_bound:

                # Move top right
                if game_board[row - 1][column + 1] is None:
                    d_movements_set.add(self.indices_to_algebraic_notation(column + 1, row - 1))

                elif game_board[row - 1][column + 1].get_player() != self.get_player():
                    d_movements_set.add(self.indices_to_algebraic_notation(column + 1, row - 1))

            # If the piece is not in the left corner.
            if column != h_lo_bound:

                # Move top left
                if game_board[row - 1][column - 1] is None:
                    d_movements_set.add(self.indices_to_algebraic_notation(column - 1, row - 1))

                elif game_board[row - 1][column - 1].get_player() != self.get_player():
                    d_movements_set.add(self.indices_to_algebraic_notation(column - 1, row - 1))

        # If the piece is on the left edge
        if column == h_lo_bound:

            # If the piece is not in the top corner.
            if row != v_lo_bound:

                # Move top right
                if game_board[row - 1][column + 1] is None:
                    d_movements_set.add(self.indices_to_algebraic_notation(column + 1, row - 1))

                elif game_board[row - 1][column + 1].get_player() != self.get_player():
                    d_movements_set.add(self.indices_to_algebraic_notation(column + 1, row - 1))

            # If the piece is not in the bottom corner.
            if row != v_hi_bound:

                # Move bottom right
                if game_board[row + 1][column + 1] is None:
                    d_movements_set.add(self.indices_to_algebraic_notation(column + 1, row + 1))

                elif game_board[row + 1][column + 1].get_player() != self.get_player():
                    d_movements_set.add(self.indices_to_algebraic_notation(column + 1, row + 1))

        # If the piece is on the right edge
        if column == h_hi_bound:

            # If the piece is not in the top corner.
            if row != v_lo_bound:

                # Move top left
                if game_board[row - 1][column - 1] is None:
                    d_movements_set.add(self.indices_to_algebraic_notation(column - 1, row - 1))

                elif game_board[row - 1][column - 1].get_player() != self.get_player():
                    d_movements_set.add(self.indices_to_algebraic_notation(column - 1, row - 1))

            # If the piece is not in the bottom corner.
            if row != v_hi_bound:

                # Move bottom left
                if game_board[row + 1][column - 1] is None:
                    d_movements_set.add(self.indices_to_algebraic_notation(column - 1, row + 1))

                elif game_board[row + 1][column - 1].get_player() != self.get_player():
                    d_movements_set.add(self.indices_to_algebraic_notation(column - 1, row + 1))

        return d_movements_set


class Soldier(JanggiPiece):
    """
    A soldier JanggiPiece that can move one space forward or one space horizontally. It cannot go backwards.

    This class inherits from JanggiPiece, since all pieces need to belong to a player and be at a position.
    """

    def __init__(self, player, position):
        """
        Initializes a soldier piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)
        self._piece_type = "soldier"

    def valid_movements(self, game_board):
        """
        Checks all possible movements on the game board and returns a set of only valid movements.
        """

        valid_movements_set = self.horizontal_movement_check(game_board)

        # Red can only move to a higher index (down the board), while blue can only move to a lower index (up the board)
        # Stop running if the piece is already at the top/bottom edge.
        if self.get_player() == "red":
            valid_movements_set.update(
                self.vertical_movement_check(game_board, self.numeric_to_index(self.get_position()), 9))

        else:
            valid_movements_set.update(
                self.vertical_movement_check(game_board, 0, self.numeric_to_index(self.get_position())))

        return valid_movements_set


class Guard(JanggiPiece):
    """
    A guard JanggiPiece that can move one space vertically or horizontally. It is only able to move within the palace.

    This class inherits from JanggiPiece, since all pieces need to belong to a player and be at a position.
    """

    def __init__(self, player, position):
        """
        Initializes a guard piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)
        self._piece_type = "guard"

    def valid_movements(self, game_board):
        """
        Checks all possible movements on the game board and returns a set of only valid movements.
        """

        column = self.alphabetic_to_index(self.get_position())
        row = self.numeric_to_index(self.get_position())
        valid_movements_set = self.horizontal_movement_check(game_board, 3, 5)

        if self.get_player() == "red":
            valid_movements_set.update(self.vertical_movement_check(game_board, 0, 2))

            # If the piece is in the corners of the red palace.
            if (row == 0 or row == 2) and (column == 3 or column == 5):
                valid_movements_set.update(self.diagonal_movement_check(game_board, 3, 5, 0, 2))

            # If the piece is in the middle of the red palace.
            elif row == 1 and column == 4:
                valid_movements_set.update(self.diagonal_movement_check(game_board, 3, 5, 0, 2))

        else:
            valid_movements_set.update(self.vertical_movement_check(game_board, 7, 9))

            # If the piece is in the corners of the blue palace.
            if (row == 7 or row == 9) and (column == 3 or column == 5):
                valid_movements_set.update(self.diagonal_movement_check(game_board, 3, 5, 7, 9))

            # If the piece is in the middle of the blue palace.
            elif row == 8 and column == 4:
                valid_movements_set.update(self.diagonal_movement_check(game_board, 3, 5, 7, 9))

        return valid_movements_set


class General(Guard):
    """
    A general JanggiPiece that can move one space vertically or horizontally. It is only able to move within the palace.
    The player loses if his general is checkmated.

    This class inherits from JanggiPiece, since all pieces need to belong to a player and be at a position.
    This class also inherits from Guard, since they are have the same move set restrictions.
    """

    def __init__(self, player, position):
        """
        Initializes a general piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)
        self._piece_type = "general"


class Horse(JanggiPiece):
    """
    A horse JanggiPiece that can move one space vertically or horizontally and then one space diagonally forwards.
    This piece cannot jump over other pieces. It cannot move in a direction if there is a piece blocking it.

    This class inherits from JanggiPiece, since all pieces need to belong to a player and be at a position.
    """

    def __init__(self, player, position):
        """
        Initializes a horse piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)
        self._piece_type = "horse"

    def valid_movements(self, game_board):
        """
        Checks all possible movements on the game board and returns a set of only valid movements.
        """
        column = self.alphabetic_to_index(self.get_position())
        row = self.numeric_to_index(self.get_position())
        valid_movements_set = set()

        # Positions the horse piece is able to move horizontally and vertically.
        hv_movements_set = self.horizontal_movement_check(game_board)
        hv_movements_set.update(self.vertical_movement_check(game_board))

        # Add to a set all the possible diagonal movements at each empty vertical/horizontal location.
        for position in hv_movements_set:
            if game_board[self.numeric_to_index(position)][self.alphabetic_to_index(position)] is None:
                temp_piece = Horse(self.get_player(), position)
                valid_movements_set.update(temp_piece.diagonal_movement_check(game_board))

        # The piece cannot move backwards diagonally. If it shares the same row or column, remove it from the set.
        for position in valid_movements_set.copy():
            if row == self.numeric_to_index(position) or column == self.alphabetic_to_index(position):
                valid_movements_set.remove(position)

        return valid_movements_set


class Elephant(Horse):
    """
    An elephant JanggiPiece that can move one space vertically or horizontally and then two spaces diagonally forward.
    This piece cannot jump over other pieces. It cannot move in a direction if there is a piece blocking it.

    This class inherits from JanggiPiece, since all pieces need to belong to a player and be at a position.
    This class also inherits from Horse, since an elephant piece uses a slightly modified version of the horse's
    movement.
    """

    def __init__(self, player, position):
        """
        Initializes an elephant piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)
        self._piece_type = "elephant"

    def valid_movements(self, game_board):
        """
        Checks all possible movements on the game board and returns a set of only valid movements.
        """
        column = self.alphabetic_to_index(self.get_position())
        row = self.numeric_to_index(self.get_position())
        valid_movements_set = set()
        horse_movements_set = super().valid_movements(game_board)
        hv_movements_set = self.horizontal_movement_check(game_board)
        hv_movements_set.update(self.vertical_movement_check(game_board))

        # Add to a set all the possible diagonal movements at each empty location.
        for position in horse_movements_set.copy():
            if game_board[self.numeric_to_index(position)][self.alphabetic_to_index(position)] is None:
                temp_piece = Elephant(self.get_player(), position)
                valid_movements_set.update(temp_piece.diagonal_movement_check(game_board))

        # Removes invalid diagonal movements.
        for position in valid_movements_set.copy():
            if row == self.numeric_to_index(position) or column == self.alphabetic_to_index(position):
                valid_movements_set.remove(position)

            else:
                for hv_position in hv_movements_set:
                    if self.numeric_to_index(hv_position) == self.numeric_to_index(position) or self.alphabetic_to_index(hv_position) == self.alphabetic_to_index(position):
                        valid_movements_set.remove(position)

        return valid_movements_set


class Chariot(JanggiPiece):
    """
    A chariot JanggiPiece that can move an the length of the board vertically or horizontally. The chariot can also move
    along the diagonal lines when in the palace.

    This class inherits from JanggiPiece, since all pieces need to belong to a player and be at a position.
    """

    def __init__(self, player, position):
        """
        Initializes a chariot piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)
        self._piece_type = "chariot"

    def inf_hv_movement(self, game_board):
        """
        Adds each space up, down, left, and right from the piece to a set until it reaches the edge or another piece.
        If it reaches a piece, it will also add its position to the set.

        Takes the game board in order to check piece positions.
        Returns a set of all positions found to be None and the first piece that is encountered in each direction.
        """
        column = self.alphabetic_to_index(self.get_position())
        row = self.numeric_to_index(self.get_position())
        hv_movements_set = set()

        # Iterate left from piece if the first space to the left is not a piece.
        if column > 0 and game_board[row][column - 1] is not None:
            hv_movements_set.add(self.indices_to_algebraic_notation(column - 1, row))
        else:
            while column > 0 and game_board[row][column - 1] is None:
                column -= 1
                hv_movements_set.add(self.indices_to_algebraic_notation(column, row))
                if column > 0 and game_board[row][column - 1] is not None:
                    hv_movements_set.add(self.indices_to_algebraic_notation(column - 1, row))

        column = self.alphabetic_to_index(self.get_position())

        # Iterate right from piece if the first space to the right is not a piece.
        if column < 8 and game_board[row][column + 1] is not None:
            hv_movements_set.add(self.indices_to_algebraic_notation(column + 1, row))
        else:
            while column < 8 and game_board[row][column + 1] is None:
                column += 1
                hv_movements_set.add(self.indices_to_algebraic_notation(column, row))
                if column < 8 and game_board[row][column + 1] is not None:
                    hv_movements_set.add(self.indices_to_algebraic_notation(column + 1, row))

        column = self.alphabetic_to_index(self.get_position())

        # Iterate up from piece if the first space up is not a piece.
        if row > 0 and game_board[row - 1][column] is not None:
            hv_movements_set.add(self.indices_to_algebraic_notation(column, row - 1))
        else:
            while row > 0 and game_board[row - 1][column] is None:
                row -= 1
                hv_movements_set.add(self.indices_to_algebraic_notation(column, row))
                if row > 0 and game_board[row - 1][column] is not None:
                    hv_movements_set.add(self.indices_to_algebraic_notation(column, row - 1))

        row = self.numeric_to_index(self.get_position())

        # Iterate down from piece if the first space down is not a piece.
        if row < 9 and game_board[row + 1][column] is not None:
            hv_movements_set.add(self.indices_to_algebraic_notation(column, row + 1))
        else:
            while row < 9 and game_board[row + 1][column] is None:
                row += 1
                hv_movements_set.add(self.indices_to_algebraic_notation(column, row))
                if row < 9 and game_board[row + 1][column] is not None:
                    hv_movements_set.add(self.indices_to_algebraic_notation(column, row + 1))

        return hv_movements_set

    def valid_movements(self, game_board):
        """
        Checks all possible movements on the game board and returns a set of only valid movements.
        """

        column = self.alphabetic_to_index(self.get_position())
        row = self.numeric_to_index(self.get_position())
        valid_movements_set = self.inf_hv_movement(game_board)

        # Look for positions with a piece in it. If it is the player's piece, remove it from the set.
        for position in valid_movements_set.copy():
            if game_board[self.numeric_to_index(position)][self.alphabetic_to_index(position)] is not None:
                if game_board[self.numeric_to_index(position)][self.alphabetic_to_index(position)].get_player() == self.get_player():
                    valid_movements_set.remove(position)

        # Diagonal movements available when inside a palace.
        # If the piece is in the corners of the red palace.
        if (row == 0 or row == 2) and (column == 3 or column == 5):
            valid_movements_set.update(self.diagonal_movement_check(game_board, 3, 5, 0, 2))

            # Possible for the piece to move an additional space diagonally if the middle of the palace is empty.
            if game_board[1][4] is None:
                temp_piece = Chariot(self.get_player(), "e2")
                temp_set = temp_piece.diagonal_movement_check(game_board)

                # Removes invalid diagonal movements.
                for temp_position in temp_set.copy():
                    if row == self.numeric_to_index(temp_position) or column == self.alphabetic_to_index(temp_position):
                        temp_set.remove(temp_position)

                valid_movements_set.update(temp_set)

        # If the piece is in the middle of the red palace.
        elif row == 1 and column == 4:
            valid_movements_set.update(self.diagonal_movement_check(game_board, 3, 5, 0, 2))

        # If the piece is in the corners of the blue palace.
        if (row == 7 or row == 9) and (column == 3 or column == 5):
            valid_movements_set.update(self.diagonal_movement_check(game_board, 3, 5, 7, 9))

            # Possible for the piece to move an additional space diagonally if the middle of the palace is empty.
            if game_board[8][4] is None:
                temp_piece = Chariot(self.get_player(), "e9")
                temp_set = temp_piece.diagonal_movement_check(game_board)

                # Removes invalid diagonal movements.
                for temp_position in temp_set.copy():
                    if row == self.numeric_to_index(temp_position) or column == self.alphabetic_to_index(temp_position):
                        temp_set.remove(temp_position)

                valid_movements_set.update(temp_set)

        # If the piece is in the middle of the blue palace.
        elif row == 8 and column == 4:
            valid_movements_set.update(self.diagonal_movement_check(game_board, 3, 5, 7, 9))

        return valid_movements_set


class Cannon(Chariot):
    """
    A cannon JanggiPiece that can only move vertically or horizontally if there is a piece in the same row/column that
    it can jump over. It can move any distance provided the previous requirement is met. It cannot capture other cannon
    pieces. It cannot jump over two pieces. The cannon can also move along the diagonal lines when in the palace.

    This class inherits from JanggiPiece, since all pieces need to belong to a player and be at a position.
    This class also inherits from Chariot, since a cannon piece uses a slightly modified version of the chariot's
    movement.
    """

    def __init__(self, player, position):
        """
        Initializes a cannon piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)
        self._piece_type = "cannon"

    def valid_movements(self, game_board):
        """
        Checks all possible movements on the game board and returns a set of only valid movements.
        """
        column = self.alphabetic_to_index(self.get_position())
        row = self.numeric_to_index(self.get_position())
        piece_location_set = self.inf_hv_movement(game_board)
        valid_movements_set = set()

        # Look for squares with pieces.
        for position in piece_location_set.copy():
            if game_board[self.numeric_to_index(position)][self.alphabetic_to_index(position)] is None:
                piece_location_set.remove(position)

            # Unable to jump over other cannons
            if game_board[self.numeric_to_index(position)][self.alphabetic_to_index(position)] is not None:
                if game_board[self.numeric_to_index(position)][self.alphabetic_to_index(position)].get_piece_name() == self.get_piece_name():
                    piece_location_set.remove(position)

        # Create a temporary piece in each location and get its vertical and horizontal movements.
        for position in piece_location_set:
            temp_piece = Cannon(self.get_player(), position)
            temp_set = temp_piece.inf_hv_movement(game_board)

            for temp_position in temp_set:

                # The cannon must move to a space within the same row or column.
                # The space must also be after the piece, since the cannon is jumping over it.
                if row == self.numeric_to_index(temp_position):

                    if self.alphabetic_to_index(temp_position) < self.alphabetic_to_index(position) < column:
                        valid_movements_set.add(temp_position)

                    elif self.alphabetic_to_index(temp_position) > self.alphabetic_to_index(position) > column:
                        valid_movements_set.add(temp_position)

                if column == self.alphabetic_to_index(position):

                    if self.numeric_to_index(temp_position) < self.numeric_to_index(position) < row:
                        valid_movements_set.add(temp_position)

                    if self.numeric_to_index(temp_position) > self.numeric_to_index(position) > row:
                        valid_movements_set.add(temp_position)

        # Cannot capture your own pieces.
        for position in valid_movements_set.copy():
            if game_board[self.numeric_to_index(position)][self.alphabetic_to_index(position)] is not None:
                if game_board[self.numeric_to_index(position)][self.alphabetic_to_index(position)].get_player() == self.get_player():
                    valid_movements_set.remove(position)

        # Diagonal movements available when inside a palace.
        # If the piece is in the corners of the red palace.
        if (row == 0 or row == 2) and (column == 3 or column == 5):
            if game_board[1][4] is not None and game_board[1][4].get_piece_name() != "cannon":
                temp_piece = Cannon(self.get_player(), "e2")
                temp_set = temp_piece.diagonal_movement_check(game_board)

                for temp_position in temp_set.copy():
                    if row == self.numeric_to_index(temp_position) or column == self.alphabetic_to_index(temp_position):
                        temp_set.remove(temp_position)

                valid_movements_set.update(temp_set)

        # If the piece is in the corners of the blue palace.
        if (row == 7 or row == 9) and (column == 3 or column == 5):
            if game_board[8][4] is not None and game_board[8][4].get_piece_name() != "cannon":
                temp_piece = Cannon(self.get_player(), "e9")
                temp_set = temp_piece.diagonal_movement_check(game_board)

                for temp_position in temp_set.copy():
                    if row == self.numeric_to_index(temp_position) or column == self.alphabetic_to_index(temp_position):
                        temp_set.remove(temp_position)

                valid_movements_set.update(temp_set)

        return valid_movements_set
