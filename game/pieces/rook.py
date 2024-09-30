from piece import Piece

class Rook(Piece):

    # Representación de la torre en el tablero
    def __str__(self):
        # Si es blanca, retorna 'R', de lo contrario 'r'
        return 'R' if self._color == 'WHITE' else 'r'
    
    # Movimientos posibles de la torre
    def possible_moves(self, from_row, from_col):
        # Direcciones verticales y horizontales
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # Llamada a la función general de movimientos
        return super().possible_moves_general(from_row, from_col, directions)
