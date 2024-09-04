from piece import Piece, Rook, Bishop

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def basic_queen_moves(self, row, col):
        # Movimientos de la reina (combinación de torre y alfil)
        rook_moves = Rook(self.color).basic_rook_moves(row, col)
        bishop_moves = Bishop(self.color).basic_bishop_moves(row, col)
        return rook_moves + bishop_moves

    @property
    def white_str(self):
        return "♕"

    @property
    def black_str(self):
        return "♛"
