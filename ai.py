from connect4 import Connect4
from player import EmptyPlayer
import numpy as np


class AI:
    def __init__(self, player):
        self._player = player

    def get_column(self, board, other_player):
        optimizer = AIMove(board, self._player, other_player)
        move = optimizer.optimal_move()

        return move.move


class AIMove:
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
        if self._value is None:
            if self._depth < self.DEPTH_THRESHOLD:
                self._value = self._evaluate()
            else:
                self._value = self._early_evaluation()

        return self._value

    def _early_evaluation(self):
        return Connect4.get_available_combinations(self._player.highlight_possible(self._board))

    def _evaluate(self):
        available_columns = Connect4.get_available_columns(
            EmptyPlayer.highlight_board(self._board)
        )

        if len(available_columns) == 0:
            return 0

        for column in available_columns:
            if self._is_move_winning(column):
                return self._calculate_max()

        alpha, beta = self._alpha, self._beta

        max_value = self._calculate_max() - 2

        if max_value < beta:
            beta = max_value
            if alpha >= beta:
                return beta

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
        empty_cells = EmptyPlayer.highlight_board(self._board)
        columns = Connect4.get_available_columns(empty_cells)

        moves = [
            AIMove(
                Connect4.add_to_column(self._board, col, EmptyPlayer.char, self._player.char),
                current_player=self._player_next,
                next_player=self._player,
                move=col,
                depth=self._depth + 1,
            ) for col in columns
        ]

        for move in moves:
            if self._is_winning(move._board):
                return move

        max_value, best_move = -np.inf, self

        for move in moves:
            if -move.evaluate() > max_value:
                max_value, best_move = -move.evaluate(), move

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

