from .piece import Piece
from .constants import QUEEN_KING_DIRECTIONS  # Importar las direcciones comunes

class Queen(Piece):

    def __init__(self, color):
        super().__init__(color)
        self._queen_king_directions = QUEEN_KING_DIRECTIONS  # Usar la constante de direcciones

    def __str__(self):
        return 'Q' if self._color_ == 'WHITE' else 'q'

    def possible_moves(self, from_row, from_col):
        directions = self._queen_king_directions
        return super().possible_moves_general(from_row, from_col, directions)
