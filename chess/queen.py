from .piece import Piece

class Queen(Piece):

    # Constructor para inicializar las direcciones de la reina
    def __init__(self, color):
        super().__init__(color)
        # Definir las direcciones posibles: combina las direcciones de torre y alfil
        self._queen_king_directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Movimientos rectilíneos (como torre)
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Movimientos diagonales (como alfil)
        ]

    # Representación de la reina en el tablero
    def __str__(self):
        # Si es blanca, retorna 'Q', de lo contrario 'q'
        return 'Q' if self._color_ == 'WHITE' else 'q'

    # Movimientos posibles de la reina
    def possible_moves(self, from_row, from_col):
        # Usa las direcciones combinadas de la torre y el alfil
        directions = self._queen_king_directions
        return super().possible_moves_general(from_row, from_col, directions)
