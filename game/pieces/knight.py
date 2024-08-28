from piece import Piece

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def basic_knight_moves(self, row, col):
        # Movimientos en L
        possible_moves = [
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (2, 1), (1, 2), (-1, 2), (-2, 1)
        ]
        moves = [(row + dr, col + dc) for dr, dc in possible_moves
                 if 0 <= row + dr < 8 and 0 <= col + dc < 8]
        return moves
    
    withe_str = "♘"
    black_str="♞"