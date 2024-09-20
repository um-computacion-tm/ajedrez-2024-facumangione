from piece import Piece

class Queen(Piece):
    white_str = "♕"
    black_str = "♛"

    def get_possible_positions(self, from_row, from_col):
        # La reina combina los movimientos ortogonales de la torre y diagonales del alfil
        possibles = (
            self.possible_orthogonal_positions(from_row, from_col)
            + self.possible_diagonal_positions(from_row, from_col)
        )
        return possibles

    def basic_queen_moves(self, row, col):
        # Definir todas las direcciones en las que se puede mover la reina
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Diagonales y arriba
            (0, -1),         (0, 1),     # Izquierda y derecha
            (1, -1), (1, 0), (1, 1)      # Diagonales y abajo
        ]

        moves = []
        for direction_r, direction_c in directions:
            for step in range(1, 8):  # La reina puede moverse cualquier número de casillas en una dirección
                r, c = row + direction_r * step, col + direction_c * step
                if 0 <= r < 8 and 0 <= c < 8:  # Asegurarse de que el movimiento esté dentro del tablero
                    moves.append((r, c))
                else:
                    break  # Detenerse si la posición está fuera del tablero

        return moves
