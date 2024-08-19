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
        
    def movimientos_basicos_de_torres(self, row, col):
        # Generar los movimientos de la torre
        moves = self.__generate_vertical_moves(row, col)
        moves.extend(self.__generate_horizontal_moves(row, col))
        
        return moves
    
    def __generate_vertical_moves(self, row, col):
        vertical_moves = [(r, col) for r in range(8) if r != row]
        return vertical_moves
    
    def __generate_horizontal_moves(self, row, col):
        horizontal_moves = [(row, c) for c in range(8) if c != col]
        return horizontal_moves



class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "PAWN"


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "KNIGHT"
        

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__="Queen"
