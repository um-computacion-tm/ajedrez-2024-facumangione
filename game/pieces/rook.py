from piece import Piece

class Rook(Piece):
    white_str = "♖"
    black_str = "♜"

    def get_possible_positions(self, from_row, from_col):
        # La torre solo se mueve en direcciones ortogonales (filas y columnas)
        possibles = self.possible_orthogonal_positions(from_row, from_col)
        return possibles

    def basic_rook_moves(self, row, col):
        # Definir las direcciones en las que se puede mover la torre (vertical y horizontal)
        directions = [
            (-1, 0),  # Arriba
            (1, 0),   # Abajo
            (0, -1),  # Izquierda
            (0, 1)    # Derecha
        ]

        moves = []
        for direction_r, direction_c in directions:
            for step in range(1, 8):  # La torre puede moverse cualquier número de casillas en una dirección
                r, c = row + direction_r * step, col + direction_c * step
                if 0 <= r < 8 and 0 <= c < 8:  # Asegurarse de que el movimiento esté dentro del tablero
                    moves.append((r, c))
                else:
                    break  # Detenerse si la posición está fuera del tablero

        return moves
