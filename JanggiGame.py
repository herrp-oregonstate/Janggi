# Author: Paul Herr
# Date: 3/1/21
# Description:


class Soldier:
    """

    """

    pass


class Guard(Soldier):
    """

    """

    pass


class General(Guard):
    """

    """

    pass


class Horse:
    """

    """

    pass


class Elephant(Horse):
    """

    """

    pass


class Chariot:
    """

    """

    pass


class Cannon(Chariot):
    """

    """

    pass


class JangiGame:
    """

    """

    def __init__(self):
        """

        """
        self._game_board = [
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],

        ]

        self._game_board2 = {
            "a1": None, "b1": None, "c1": None, "d1": None, "e1": None, "f1": None, "g1": None, "h1": None, "i1": None,
            "a2": None, "b2": None, "c2": None, "d2": None, "e2": None, "f2": None, "g2": None, "h2": None, "i2": None,
            "a3": None, "b3": None, "c3": None, "d3": None, "e3": None, "f3": None, "g3": None, "h3": None, "i3": None,
            "a4": None, "b4": None, "c4": None, "d4": None, "e4": None, "f4": None, "g4": None, "h4": None, "i4": None,
            "a5": None, "b5": None, "c5": None, "d5": None, "e5": None, "f5": None, "g5": None, "h5": None, "i5": None,
            "a6": None, "b6": None, "c6": None, "d6": None, "e6": None, "f6": None, "g6": None, "h6": None, "i6": None,
            "a7": None, "b7": None, "c7": None, "d7": None, "e7": None, "f7": None, "g7": None, "h7": None, "i7": None,
            "a8": None, "b8": None, "c8": None, "d8": None, "e8": None, "f8": None, "g8": None, "h8": None, "i8": None,
            "a9": None, "b9": None, "c9": None, "d9": None, "e9": None, "f9": None, "g9": None, "h9": None, "i9": None,
            "a10": None, "b10": None, "c10": None, "d10": None, "e10": None, "f10": None, "g10": None, "h10": None,
            "i10": None
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

    def algebraic_notation_to_list(self, algebraic_notation):
        """

        :param algebraic_notation:
        :return:
        """

        pass
