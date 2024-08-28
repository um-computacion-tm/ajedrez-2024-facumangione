from piece import Piece

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def basic_bishop_moves(self, row, col):
        # Movimientos diagonales
        moves = []
        for delta in range(1, 8):
            moves += [
                (row + delta, col + delta),
                (row + delta, col - delta),
                (row - delta, col + delta),
                (row - delta, col - delta)
            ]
        # Filtrar movimientos fuera del tablero
        moves = [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]
        return moves
    
    withe_str = "♗"
    black_str="♝"