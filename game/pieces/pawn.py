from piece import Piece

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def basic_pawn_moves(self, row, col):
        moves = []
        if self.color == "BLACK":
            if row < 7:
                moves.append((row + 1, col))
            if row == 1:
                moves.append((row + 2, col))
        else:  # Para los peones blancos
            if row > 0:
                moves.append((row - 1, col))
            if row == 6:
                moves.append((row - 2, col))
        return moves
    
    def eat_pieces_with_peon(self, row, col):
        moves = []
        if self.color == "WHITE":
            moves = [(row - 1, col - 1), (row - 1, col + 1)]
        elif self.color == "BLACK":
            moves = [(row + 1, col - 1), (row + 1, col + 1)]
        return moves

    @property
    def white_str(self):
        return "♙"

    @property
    def black_str(self):
        return "♟"
