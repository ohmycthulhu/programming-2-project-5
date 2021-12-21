import numpy as np


class Connect4:
    # All winning combinations
    # Matrices are applied the way that all cells are checked at least one
    VERTICAL_WIN = np.array([[1], [1], [1], [1]])
    HORIZONTAL_WIN = np.array([[1, 1, 1, 1]])
    DIAGONAL_WIN = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    REVERSE_DIAGONAL_WIN = np.array([[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]])

    # This list contains all matrices that are needed to be checked
    CONDITION_MATRICES = [VERTICAL_WIN, HORIZONTAL_WIN, DIAGONAL_WIN, REVERSE_DIAGONAL_WIN]

    @staticmethod
    def check_winner(board_bool):
        return np.any([
            Connect4._compliant_to_matrix(board_bool, cond) for cond in Connect4.CONDITION_MATRICES
        ])

    # This function applies matrix for checking the winning combination
    # The matrix shape should be less or equal in each dimension
    # The idea behind check is simple - we take submatrix from the board and check the following condition:
    # If each 1 value of matrix matches with True in submatrix
    # In this case, sum of result will be the same as sum of matrix itself
    @staticmethod
    def _compliant_to_matrix(board, matrix):
        m_h, m_w = matrix.shape
        b_h, b_w = board.shape
        purp_sum = np.sum(matrix)

        for i in range(b_h - m_h + 1):
            for j in range(b_w - m_w + 1):
                part = board[i:(i+m_h), j:(j+m_w)]
                if np.sum(part & matrix) == purp_sum:
                    return True

        return False

    @staticmethod
    def get_available_columns(board_bool):
        return [i for i in range(board_bool.shape[1]) if board_bool[0, i]]

    @staticmethod
    def get_available_combinations(board_bool):
        return Connect4._get_available_vertical(board_bool) + \
            Connect4._get_available_horizontal(board_bool) + \
            Connect4._get_available_diagonal(board_bool)

    @staticmethod
    def _get_available_horizontal(board_bool):
        result = 0
        height, width = board_bool.shape
        for i in range(height):
            for j in range(width - 3):
                if board_bool[i, j] and board_bool[i, j + 1] and \
                        board_bool[i, j + 2] and board_bool[i, j + 3]:
                    result += 1
        return result

    @staticmethod
    def _get_available_vertical(board_bool):
        result = 0
        height, width = board_bool.shape
        for i in range(height - 3):
            for j in range(width):
                if board_bool[i, j] and board_bool[i + 1, j] and \
                        board_bool[i + 2, j] and board_bool[i + 3, j]:
                    result += 1
        return result

    @staticmethod
    def _get_available_diagonal(board_bool):
        result = 0
        height, width = board_bool.shape
        for i in range(min(height, width) - 3):
            for j in range(min(height, width) - 3):
                if board_bool[i, j] and board_bool[i + 1, j + 1] and \
                        board_bool[i + 2, j + 2] and board_bool[i + 3, j + 3]:
                    result += 1
                if board_bool[i + 3, j] and board_bool[i + 2, j + 1] and \
                        board_bool[i + 1, j + 2] and board_bool[i, j + 3]:
                    result += 1
        return result
