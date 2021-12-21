import numpy as np


class Board:
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
        if not self.can_add_element(column):
            return False

        col = self._board[:, column]

        for i in range(len(col) - 1, -1, -1):
            if col[i] == self._default:
                print('Setting char')
                self._board[i, column] = char
                break

        return True

    def can_add_element(self, column):
        if column < 0 or column >= self._board.shape[1]:
            return False
        col = self._board[:, column]
        return np.any(col == self._default)

    def get_board(self):
        return np.copy(self._board)

    def has_free_cell(self):
        return np.any(self._board == self._default)
