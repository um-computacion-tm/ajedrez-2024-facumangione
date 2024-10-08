from chess.piece import Piece

class Knight(Piece):

    # Método que representa al caballero en el tablero
    def __str__(self):
        #Devuelve 'N' si el caballero es blanco y 'n' si es negro.
        return 'N' if self._color_ == 'WHITE' else 'n'

    # Método que genera las direcciones de movimiento del caballero
    def generate_knight_directions(self):
        #Devuelve una lista de direcciones en las que el caballero puede moverse.
        directions = []
        moves = [2, 1, -1, -2]
        for i in moves:
            for j in moves:
                if abs(i) != abs(j):
                    directions.append((i, j))
        return directions

    # Método que devuelve los movimientos posibles del caballero
    def possible_moves(self, from_row, from_col):

        # Devuelve los movimientos posibles del caballero desde una posición actual.
        # Utiliza las direcciones generadas por generate_knight_directions.
    
        directions = self.generate_knight_directions()
        return self.possible_moves_general(from_row, from_col, directions)
