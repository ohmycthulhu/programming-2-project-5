import numpy as np


class Board:
    """
        Responsible for managing the board in abstract way.
        Implements adding to the column and checking if there are empty cells
    """
    def __init__(self, rows, cols, default_value):
        self._board = np.array([[default_value for _ in range(cols)] for _ in range(rows)])
        self._default = default_value

    def print(self):
        height, width = self._board.shape

        # Print the board
        for i in range(height):
            print('', *self._board[i, :], '', sep=' | ')

        print(' ', '-' * 4 * width, sep='')
        print('', *[i + 1 for i in range(width)], '', sep=' | ')

    def add_element(self, column, char):
        if not self._can_add_element(column):
            return False

        col = self._board[:, column]

        # range(len(col) - 1, -1, -1) will give sequence [6, 5, 4, 3, 2, 1, 0] for len(col) = 7
        for i in range(len(col) - 1, -1, -1):
            if col[i] == self._default:
                self._board[i, column] = char
                break

        return True

    def _can_add_element(self, column):
        if column < 0 or column >= self._board.shape[1]:
            return False
        col = self._board[:, column]
        return np.any(col == self._default)

    @property
    def board(self):
        return np.copy(self._board)

    @property
    def has_free_cell(self):
        return np.any(self._board == self._default)
