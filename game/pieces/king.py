from piece import Piece

class King(Piece):

    # Representación del rey en el tablero
    def __str__(self):
        # Si es blanco, retorna 'K', de lo contrario 'k'
        return 'K' if self._color == 'WHITE' else 'k'
    
    # Movimientos posibles del rey
    def possible_moves(self, from_row, from_col):
        # Usa las mismas direcciones que la reina pero con un solo paso
        directions = self._queen_king_directions
        return super().possible_moves_general(from_row, from_col, directions, single_step=True)
