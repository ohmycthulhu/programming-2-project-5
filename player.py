class Player:
    def __init__(self, name, character, is_playable=True):
        self.name = name
        self.char = character

    def highlight_board(self, board):
        return board == self.char

    def get_char(self):
        return self.char

    def get_name(self):
        return self.name


EmptyPlayer = Player('Empty cell', ' ', is_playable=False)
