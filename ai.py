from connect4 import Connect4
from player import EmptyPlayer
import numpy as np


class AI:
    """Class for generating new moves. It's stateless so it's easier to manage"""
    def __init__(self, player):
        self._player = player

    def get_next_move(self, board, other_player):
        optimizer = AIMove(board, self._player, other_player)
        move = optimizer.optimal_move()

        return move.move


class AIMove:
    """Represent current move and holds the ability to generate optimal solution"""
    DEPTH_THRESHOLD = 4

    def __init__(self, board, current_player, next_player, move=None, alpha=-np.inf, beta=np.inf, depth=0):
        self._move = move
        self._board = board
        self._alpha = alpha
        self._beta = beta
        self._player = current_player
        self._player_next = next_player
        self._value = None
        self._depth = depth

    def evaluate(self):
        # Function with memoization, so it won't repeat complex computations
        if self._value is None:
            # If it's reached too deep, use early evaluation
            if self._depth < self.DEPTH_THRESHOLD:
                self._value = self._evaluate()
            else:
                self._value = self._early_evaluation()

        return self._value

    def _early_evaluation(self):
        return Connect4.get_available_combinations(self._player.highlight_possible(self._board))

    def _evaluate(self):
        # Get all possible moves
        available_columns = Connect4.get_available_columns(
            EmptyPlayer.highlight_board(self._board)
        )

        if len(available_columns) == 0:
            return 0

        # If there is a winning move, return max value
        for column in available_columns:
            if self._is_move_winning(column):
                return self._calculate_max()

        # Manage alpha and beta values, and store separately to update it after
        alpha, beta = self._alpha, self._beta

        max_value = self._calculate_max() - 2

        if max_value < beta:
            beta = max_value
            if alpha >= beta:
                return beta

        # For every possible move, create new node in the tree and evaluate the results
        for column in available_columns:
            next_move = AIMove(
                board=Connect4.add_to_column(self._board, column, EmptyPlayer.char, self._player.char),
                current_player=self._player_next,
                next_player=self._player,
                move=column,
                alpha=alpha,
                beta=beta,
                depth=self._depth + 1,
            )

            score = -next_move.evaluate()

            if score >= beta:
                return beta

            if score > alpha:
                alpha = score

        return alpha

    def _calculate_max(self):
        return 6 * (np.sum(EmptyPlayer.highlight_board(self._board)) + 1)

    def optimal_move(self):
        # Get the possible moves
        empty_cells = EmptyPlayer.highlight_board(self._board)
        columns = Connect4.get_available_columns(empty_cells)

        # Generate new nodes for each move
        moves = [
            AIMove(
                Connect4.add_to_column(self._board, col, EmptyPlayer.char, self._player.char),
                current_player=self._player_next,
                next_player=self._player,
                move=col,
                depth=self._depth + 1,
            ) for col in columns
        ]

        # If there is a winning move, immediately return
        for move in moves:
            if self._is_winning(move._board):
                return move

        # If not, try to find the best possible way
        max_value, best_move = -np.inf, self

        for move in moves:
            value = -move.evaluate()
            if value > max_value:
                # Minus here because the next node is minimizer, so it will return negative value
                max_value, best_move = value, move

        return best_move

    def _is_move_winning(self, col):
        res_board = Connect4.add_to_column(self._board, col, EmptyPlayer.char, self._player.char)
        if res_board is None:
            raise Exception(f"Illegal move {col}")
        return self._is_winning(res_board)

    def _is_winning(self, board):
        return Connect4.get_available_combinations(self._player.highlight_board(board)) > 0

    @property
    def move(self):
        return self._move

