from game.board import Board

class Piece:
    def __init__(self, color):
        self.__color__ = color
        self.__board__ = Board()

    @property
    def color(self):
        return self.__color__

    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str

    @property
    def white_str(self):
        # Este método debe ser sobrescrito por las subclases
        raise NotImplementedError("Subclasses should implement this method")

    @property
    def black_str(self):
        # Este método debe ser sobrescrito por las subclases
        raise NotImplementedError("Subclasses should implement this method")

    def get_valid_moves(self, board, row, col):
        # Este método debe ser sobrescrito por las subclases
        raise NotImplementedError("Subclasses should implement this method")
