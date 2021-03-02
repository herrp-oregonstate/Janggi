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

    def algebraic_notation_to_list(self, algebraic_notation):
        """

        :param algebraic_notation:
        :return:
        """

        pass
