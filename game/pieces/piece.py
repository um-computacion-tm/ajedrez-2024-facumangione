from board import Board
class Piece:
    def __init__(self, color):
        self.__color__ = color
        self.__board__ = Board

    @property
    def color(self):
        return self._color
    
    def __str__(self):
        if self.__color__ == "WITHE":
            return self.white_Str
        else:
            return self.black_str
