from board import Board
from piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def basic_rook_moves(self, row, col):
        # Movimientos verticales y horizontales
        moves = [(r, col) for r in range(8) if r != row] + \
                [(row, c) for c in range(8) if c != col]
        return moves

    @property
    def white_str(self):
        return "♖"

    @property
    def black_str(self):
        return "♜"
