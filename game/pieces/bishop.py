from piece import Piece

class Bishop(Piece):

    # Método que representa el alfil en el tablero
    def __str__(self):
        
        #Devuelve 'B' si el alfil es blanco y 'b' si es negro.
        
        return 'B' if self.color == 'WHITE' else 'b'

    # Método que devuelve los movimientos posibles del alfil
    def possible_moves(self, from_row, from_col):
        
        #Devuelve una lista de movimientos posibles del alfil desde una posición inicial.
        
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Movimientos diagonales
        return self.possible_moves_general(from_row, from_col, directions)
