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
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
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

    def