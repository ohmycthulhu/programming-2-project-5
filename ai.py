from connect4 import Connect4
from player import EmptyPlayer
import numpy as np


class AI:
    def __init__(self, player):
        self._player = player

    def get_column(self, board):
        empty_cells = EmptyPlayer.highlight_board(board)
        columns = Connect4.get_available_columns(empty_cells)
        return np.random.choice(columns)

