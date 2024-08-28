from piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def basic_king_moves(self, row, col):
        # Definir las direcciones en las que se puede mover el rey
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Movimientos diagonales superiores
            (0, -1),          (0, 1),    # Movimientos horizontales
            (1, -1), (1, 0), (1, 1)      # Movimientos diagonales inferiores
        ]

        moves = []
        for direction_r, direction_c in directions:
            r, c = row + direction_r, col + direction_c
            if 0 <= r < 8 and 0 <= c < 8:  # Asegurarse de que el movimiento esté dentro del tablero
                moves.append((r, c))

        return moves
    
    withe_str = "♔"
    black_str="♚"
