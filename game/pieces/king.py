from piece import Piece

class King(Piece):
    white_str = "♔"
    black_str = "♚"

    def get_possible_positions(self, from_row, from_col):
        # Obtener las posiciones ortogonales y diagonales
        possibles = (
            self.possible_orthogonal_positions(from_row, from_col)
            + self.possible_diagonal_positions(from_row, from_col)
        )
        possible_king = []
        # Filtrar las posiciones válidas donde el rey solo puede moverse una casilla
        for possible_row, possible_col in possibles:
            if abs(from_row - possible_row) <= 1 and abs(from_col - possible_col) <= 1:
                possible_king.append((possible_row, possible_col))
        return possible_king

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
