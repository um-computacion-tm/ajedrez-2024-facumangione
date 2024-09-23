from piece import Piece

class Knight(Piece):
    white_str = "♘"
    black_str = "♞"

    def get_possible_positions(self, from_row, from_col):
        return self.basic_knight_moves(from_row, from_col)

    def basic_knight_moves(self, row, col):
        # Definir las posiciones en forma de "L" que puede tomar el caballo
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2),
        ]

        # Filtrar solo las posiciones que estén dentro del tablero
        return [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]
