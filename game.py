from board import Board
from player import Player, EmptyPlayer
from connect4 import Connect4
from ai import AI


class Game:
    def __init__(self, width, height):
        self._board = Board(rows=height, cols=width, default_value=EmptyPlayer.get_char())
        player_user = Player('Player Y', 'Y')
        player_ai = Player('Player R', 'R')
        self._players = [player_user, player_ai]
        self._ai = AI(player_ai)
        self._turn = 0
        self._winner = None

    def iterate(self):
        self._board.print()
        current_player = self._current_player

        if self._ai_should_move:
            move = self._get_ai_move()
        else:
            move = self._input_column()

        # If the input is invalid, the iteration finished, but current player stays the same
        if not self._board.can_add_element(move):
            return

        self._board.add_element(move, current_player.get_char())
        self._turn += 1

        if self._check_winner(current_player):
            self._winner = current_player

    def print(self):
        self._board.print()

    def _check_winner(self, player):
        # Convert 2D numpy board to 2D array of booleans
        # It will be easier to check this way
        board = self._board.get_board()
        board_bool = player.highlight_board(board)
        return Connect4.check_winner(board_bool)

    @property
    def winner_name(self):
        if self._winner is None:
            raise Exception("Winner is not found!")
        return self._winner.get_name()

    @property
    def _message_for_input(self):
        return self._current_player.get_name() + ": "

    def _input_column(self):
        # Result is shifted by -1, so user will input [1...] instead of [0...]
        try:
            return int(input(self._message_for_input)) - 1
        except ValueError as e:
            return -1

    def can_continue(self):
        return self._board.has_free_cell() and self._winner is None

    @property
    def _current_player(self):
        return self._players[self._turn % len(self._players)]

    def has_winner(self):
        return self._winner is not None

    @property
    def _ai_should_move(self):
        return self._turn % 2 == 1

    def _get_ai_move(self):
        return self._ai.get_column(self._board.get_board())
