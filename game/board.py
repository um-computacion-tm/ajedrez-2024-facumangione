from game.pieces.piece import Rook, Knight, Bishop, Queen, King, Pawn

class Board:
    def __init__(self, for_test=False):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        
        if not for_test:
            # Colocar las piezas negras
            self.__positions__[0][0] = Rook("BLACK", self)
            self.__positions__[0][7] = Rook("BLACK", self)
            self.__positions__[0][1] = Knight("BLACK", self)
            self.__positions__[0][6] = Knight("BLACK", self)
            self.__positions__[0][2] = Bishop("BLACK", self)
            self.__positions__[0][5] = Bishop("BLACK", self)
            self.__positions__[0][3] = Queen("BLACK", self)
            self.__positions__[0][4] = King("BLACK", self)
            for i in range(8):
                self.__positions__[1][i] = Pawn("BLACK", self)

            # Colocar las piezas blancas
            self.__positions__[7][0] = Rook("WHITE", self)
            self.__positions__[7][7] = Rook("WHITE", self)
            self.__positions__[7][1] = Knight("WHITE", self)
            self.__positions__[7][6] = Knight("WHITE", self)
            self.__positions__[7][2] = Bishop("WHITE", self)
            self.__positions__[7][5] = Bishop("WHITE", self)
            self.__positions__[7][3] = Queen("WHITE", self)
            self.__positions__[7][4] = King("WHITE", self)
            for i in range(8):
                self.__positions__[6][i] = Pawn("WHITE", self)

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str

    def get_piece(self, row, col):
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        if piece:
            self.set_piece(to_row, to_col, piece)
            self.set_piece(from_row, from_col, None)

    def place_piece(self, row, col, piece):
        self.__positions__[row][col] = piece
