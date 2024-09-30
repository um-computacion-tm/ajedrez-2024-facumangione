from piece import Piece

class Queen(Piece):

    # Representación de la reina en el tablero
    def __str__(self):
        # Si es blanca, retorna 'Q', de lo contrario 'q'
        return 'Q' if self._color == 'WHITE' else 'q'
    
    # Movimientos posibles de la reina
    def possible_moves(self, from_row, from_col):
        # Usa las direcciones combinadas de la torre y el alfil
        directions = self._queen_king_directions
        return super().possible_moves_general(from_row, from_col, directions)
