# Author: Paul Herr
# Date: 3/1/21
# Description:


class JangiGame:
    """

    """

    def __init__(self):
        """

        """
        self._game_board = [
            ["RChariot", "RElephant", "RHorse", "RGuard", None, "RGuard", "RElephant", "RHorse", "RChariot"],
            [None, None, None, None, "RGeneral", None, None, None, None],
            [None, "RCannon", None, None, None, None, None, "RCannon", None],
            ["RSoldier", None, "RSoldier", None, "RSoldier", None, "RSoldier", None, "RSoldier"],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            ["BSoldier", None, "BSoldier", None, "BSoldier", None, "BSoldier", None, "BSoldier"],
            [None, "BCannon", None, None, None, None, None, "BCannon", None],
            [None, None, None, None, "BGeneral", None, None, None, None],
            ["BChariot", "BElephant", "BHorse", "BGuard", None, "BGuard", "BElephant", "BHorse", "BChariot"],

        ]

        self._game_board2 = {
            "a1": "RChariot", "b1": "RElephant", "c1": "RHorse", "d1": "RGuard", "e1": None,
            "f1": "RGuard", "g1": "RElephant", "h1": "RHorse", "i1": "RChariot",

            "a2": None, "b2": None, "c2": None, "d2": None, "e2": "RGeneral",
            "f2": None, "g2": None, "h2": None, "i2": None,

            "a3": None, "b3": "RCannon", "c3": None, "d3": None, "e3": None,
            "f3": None, "g3": None, "h3": "RCannon", "i3": None,

            "a4": "RSoldier", "b4": None, "c4": "RSoldier", "d4": None, "e4": "RSoldier",
            "f4": None, "g4": "RSoldier", "h4": None, "i4": "RSoldier",

            "a5": None, "b5": None, "c5": None, "d5": None, "e5": None,
            "f5": None, "g5": None, "h5": None, "i5": None,

            "a6": None, "b6": None, "c6": None, "d6": None, "e6": None,
            "f6": None, "g6": None, "h6": None, "i6": None,

            "a7": "BSoldier", "b7": None, "c7": "BSoldier", "d7": None, "e7": "BSoldier",
            "f7": None, "g7": "BSoldier", "h7": None, "i7": "BSoldier",

            "a8": None, "b8": "BCannon", "c8": None, "d8": None, "e8": None,
            "f8": None, "g8": None, "h8": "BCannon", "i8": None,

            "a9": None, "b9": None, "c9": None, "d9": None, "e9": "BGeneral",
            "f9": None, "g9": None, "h9": None, "i9": None,

            "a10": "BChariot", "b10": "BElephant", "c10": "BHorse", "d10": "BGuard", "e10": None,
            "f10": "BGuard", "g10": "BElephant", "h10": "BHorse", "i10": "BChariot"
        }
        pass

    def get_game_state(self):
        """

        :return:
        """

        pass

    def make_move(self, piece_location, move_location):
        """

        :param piece_location:
        :param move_location:
        :return:
        """

        pass

    def is_in_check(self, player_color):
        """

        :param player_color:
        :return:
        """

        pass

    def get_location(self, piece):
        """

        :param piece:
        :return:
        """

        pass

    def space_is_empty(self, location):
        """

        :param location:
        :return:
        """

        pass

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

    def valid_moves(self, piece):
        """

        :param piece:
        :return:
        """

        pass


class JangiPiece(JangiGame):
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


class Soldier(JangiPiece):
    """
    A soldier piece that can move forward one space or move to the left or right one space. It cannot go backwards.
    """

    def __init__(self, player, position):
        """
        Initializes a soldier piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)

    def possible_movements(self):
        """
        Returns a set of possible movements for the soldier piece.
        """

        possible_movements_set = set()
        x_axis = self.alphabetic_to_index(self.get_position())
        y_axis = self.numeric_to_index(self.get_position())

        # Both players are able to move left or right, unless they are at the edge of the board.
        if x_axis != 0 and x_axis != 8:
            possible_movements_set.add(self.indices_to_algebraic_notation(x_axis + 1, y_axis))
            possible_movements_set.add(self.indices_to_algebraic_notation(x_axis - 1, y_axis))
        elif x_axis == 0:
            possible_movements_set.add(self.indices_to_algebraic_notation(x_axis + 1, y_axis))
        else:
            possible_movements_set.add(self.indices_to_algebraic_notation(x_axis - 1, y_axis))

        # Red can only move to a higher index (down the board), while blue can only move to a lower index (up the board)
        if self.get_player() == "red":
            if y_axis != 9:
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis, y_axis + 1))
        else:
            if y_axis != 0:
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis, y_axis - 1))

        return possible_movements_set

    pass


class Guard(JangiPiece):
    """
    A guard piece that can move forward one space, backwards one space, or left or right one space. It is only able to
    move within the palace.
    """

    def __init__(self, player, position):
        """
        Initializes a guard piece to belong to a player and sets its position on the board.:
        """

        super().__init__(player, position)

    def possible_movements(self):
        """
        Returns a set of possible movements for the soldier piece.
        """
        possible_movements_set = set()
        x_axis = self.alphabetic_to_index(self.get_position())
        y_axis = self.numeric_to_index(self.get_position())

        if self.get_player() == "red":

            # Allows horizontal movement within the red palace only.
            if x_axis != 3 and x_axis != 5:
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis + 1, y_axis))
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis - 1, y_axis))
            elif x_axis == 3:
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis + 1, y_axis))
            elif x_axis == 5:
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis - 1, y_axis))

            # Allows vertical movement within the red palace only.
            if y_axis != 0 or y_axis != 2:
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis, y_axis + 1))
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis, y_axis - 1))
            elif y_axis == 0:
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis, y_axis + 1))
            elif y_axis == 2:
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis, y_axis - 1))

        else:

            # Allows horizontal movement within the blue palace only.
            if x_axis != 3 and x_axis != 5:
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis + 1, y_axis))
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis - 1, y_axis))
            elif x_axis == 3:
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis + 1, y_axis))
            elif x_axis == 5:
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis - 1, y_axis))

            # Allows vertical movement within the blue palace only.
            if y_axis != 7 or y_axis != 9:
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis, y_axis + 1))
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis, y_axis - 1))
            elif y_axis == 9:
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis, y_axis + 1))
            elif y_axis == 7:
                possible_movements_set.add(self.indices_to_algebraic_notation(x_axis, y_axis - 1))

    pass


class General(Guard):
    """
    A general piece that can move forward one space, backwards one space, or left or right one space. It is only able to
    move within the palace. The player loses if his general is checkmated.
    """

    def __init__(self, player, position):
        """
        Initializes a general piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)

    pass


class Horse:
    """

    """

    def __init__(self, player, position):
        """
        Initializes a horse piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)

    pass


class Elephant(Horse):
    """

    """

    def __init__(self, player, position):
        """
        Initializes an elephant piece to belong to a player and sets its position on the board.
:
        """

        super().__init__(player, position)

    pass


class Chariot:
    """

    """

    def __init__(self, player, position):
        """
        Initializes a chariot piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)

    pass


class Cannon(Chariot):
    """

    """

    def __init__(self, player, position):
        """
        Initializes a cannon piece to belong to a player and sets its position on the board.
        """

        super().__init__(player, position)

    pass
