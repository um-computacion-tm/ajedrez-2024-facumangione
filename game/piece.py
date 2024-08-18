class Piece:
    def __init__(self, color):
        self.__color__ = color
        self.__type__ = None

    def get_color(self):
        return self.__color__

    def get_type(self):
        return self.__type__


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "ROOK"


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "PAWN"


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "KNIGHT"
