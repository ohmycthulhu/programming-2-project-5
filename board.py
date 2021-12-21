import numpy as np


class Board:
    def __init__(self, rows, cols, default_value):
        self.board = np.array([[default_value for _ in range(cols)] for _ in range(rows)])
        self.default = default_value

    def print(self):
        height, width = self.board.shape

        # Print the board
        for i in range(height):
            print('', *self.board[i, :], '', sep=' | ')

        print(' ', '-' * 4 * width, sep='')
        print('', *[i + 1 for i in range(width)], '', sep=' | ')

    def add_element(self, column, char):
        if not self.can_add_element(column):
            return False

        col = self.board[:, column]

        for i in range(len(col) - 1, -1, -1):
            if col[i] == self.default:
                print('Setting char')
                self.board[i, column] = char
                break

        return True

    def can_add_element(self, column):
        if column < 0 or column >= self.board.shape[1]:
            return False
        col = self.board[:, column]
        return np.any(col == self.default)

    def get_board(self):
        return np.copy(self.board)

    def has_free_cell(self):
        return np.any(self.board == self.default)
