import numpy as np


class Player:
    """
        Class for representing the player. It provides methods for accessing char, name and highlighting the board.
        Highlighting is a map: [[any]] => [[boolean]]
    """
    def __init__(self, name, character):
        self._name = name
        self._char = character

    def highlight_board(self, board):
        return board == self._char

    def highlight_possible(self, board):
        return np.logical_or(board == self._char, board == EmptyPlayer.char)

    @property
    def char(self):
        return self._char

    @property
    def name(self):
        return self._name


# Default player for representing empty cell
EmptyPlayer = Player('Empty cell', ' ')
