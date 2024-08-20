from game.board import Board


class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move(self,from_row,from_col,to_row,to_col,):

        # validate coords
        piece = self.__board__.get_piece(from_row, from_col)
        
        if piece is not None: #solo cambio el turno si hay una piece en la posicion origen
            self.__board__.__positions__[to_row][to_col] = piece #muevo la piece al destino
            self.__board__.__positions__[from_row][from_col] = None #vacio la casilla de origen
            self.change_turn()

    @property
    def turn(self):
        return self.__turn__

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"