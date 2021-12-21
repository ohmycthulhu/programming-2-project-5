import numpy as np
from board import Board
from player import Player, EmptyPlayer


class Game:
    # All winning combinations
    # Matrices are applied the way that all cells are checked at least one
    VERTICAL_WIN = np.array([[1], [1], [1], [1]])
    HORIZONTAL_WIN = np.array([[1, 1, 1, 1]])
    DIAGONAL_WIN = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    REVERSE_DIAGONAL_WIN = np.array([[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]])

    # This list contains all matrices that are needed to be checked
    CONDITION_MATRICES = [VERTICAL_WIN, HORIZONTAL_WIN, DIAGONAL_WIN, REVERSE_DIAGONAL_WIN]

    def __init__(self, size=7):
        self.size = size
        self.board = Board(size, size, EmptyPlayer.get_char())
        self.players = [Player('Player Y', 'Y'), Player('Player R', 'R')]
        self.turn = 0
        self.winner = None

    def iterate(self):
        self.board.print()
        move = self.input_column()

        # If the input is invalid, the iteration finished, but current player stays the same
        if not self.board.can_add_element(move):
            return

        current_player = self.current_player()
        self.board.add_element(move, current_player.get_char())
        self.turn += 1

        if self.check_winner(current_player):
            self.winner = current_player

    def print(self):
        self.board.print()

    def check_winner(self, player):
        # Convert 2D numpy board to 2D array of booleans
        # It will be easier to check this way
        board = self.board.get_board()
        board_bool = player.highlight_board(board)
        return np.any([self.compliant_to_matrix(board_bool, cond) for cond in self.CONDITION_MATRICES])

    # This function applies matrix for checking the winning combination
    # The matrix shape should be less or equal in each dimension
    # The idea behind check is simple - we take submatrix from the board and check the following condition:
    # If each 1 value of matrix matches with True in submatrix
    # In this case, sum of result will be the same as sum of matrix itself
    @staticmethod
    def compliant_to_matrix(board, matrix):
        m_h, m_w = matrix.shape
        b_h, b_w = board.shape
        purp_sum = np.sum(matrix)

        for i in range(b_h - m_h + 1):
            for j in range(b_w - m_w + 1):
                part = board[i:(i+m_h), j:(j+m_w)]
                if np.sum(part & matrix) == purp_sum:
                    return True

        return False

    def get_winner_name(self):
        if self.winner is None:
            raise Exception("Winner is not found!")
        return self.winner.get_name()

    def message_for_input(self):
        return self.current_player().get_name() + ": "

    def input_column(self):
        # Result is shifted by -1, so user will input [1...] instead of [0...]
        try:
            return int(input(self.message_for_input())) - 1
        except ValueError as e:
            return -1

    def can_continue(self):
        return self.board.has_free_cell() and self.winner is None

    def current_player(self):
        return self.players[self.turn % len(self.players)]

    def has_winner(self):
        return self.winner is not None
