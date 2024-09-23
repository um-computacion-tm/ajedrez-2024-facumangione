from piece import Piece

class Bishop(Piece):
    white_str = "♗"
    black_str = "♝"

    def get_possible_positions(self, from_row, from_col):
        # El alfil solo se mueve en direcciones diagonales
        possibles = self.possible_diagonal_positions(from_row, from_col)
        return possibles

    def basic_bishop_moves(self, row, col):
        # Definir las direcciones en las que se puede mover el alfil (diagonales)
        directions = [
            (-1, -1),  # Diagonal superior izquierda
            (-1, 1),   # Diagonal superior derecha
            (1, -1),   # Diagonal inferior izquierda
            (1, 1)     # Diagonal inferior derecha
        ]

        moves = []
        for direction_r, direction_c in directions:
            for step in range(1, 8):  # El alfil puede moverse cualquier número de casillas en una dirección
                r, c = row + direction_r * step, col + direction_c * step
                if 0 <= r < 8 and 0 <= c < 8:  # Asegurarse de que el movimiento esté dentro del tablero
                    moves.append((r, c))
                else:
                    break  # Detenerse si la posición está fuera del tablero

        return moves
