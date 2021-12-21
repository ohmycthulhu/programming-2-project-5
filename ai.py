from connect4 import Connect4
from player import EmptyPlayer
import numpy as np


class AI:
    def __init__(self, player):
        self._player = player

    def get_column(self, board):
        empty_cells = EmptyPlayer.highlight_board(board)
        columns = Connect4.get_available_columns(empty_cells)

        for col in columns:
            if self._is_move_winning(board, col):
                return col

        return np.random.choice(columns)

    def _is_move_winning(self, board, col):
        res_board = Connect4.add_to_column(board, col, EmptyPlayer.char, self._player.char)
        if res_board is None:
            raise Exception(f"Illegal move {col}")
        return self._is_winning(res_board)

    def _is_winning(self, board):
        return Connect4.get_available_combinations(self._player.highlight_board(board)) > 0

