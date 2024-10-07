from chess.piece import Piece

class Pawn(Piece):
    
    # Método que representa el peón en el tablero
    def __str__(self):
        # Devuelve 'P' si el peón es blanco y 'p' si es negro.
        
        return 'P' if self._color_ == 'WHITE' else 'p'
    
    # Método que devuelve los movimientos posibles del peón
    def possible_moves(self, row, col):
        #Devuelve una lista de posiciones a las que el peón puede moverse desde una posición actual.
        moves = []
        direction = -1 if self._color_ == 'WHITE' else 1
        start_row = 6 if self._color_ == 'WHITE' else 1

        # Movimiento hacia adelante
        moves.append((row + direction, col))
        
        # Movimiento de dos espacios desde la posición inicial
        if row == start_row:
            moves.append((row + 2 * direction, col))

        # Movimientos diagonales para capturar piezas
        if row != start_row:  # Sólo si no está en la posición inicial
            moves.append((row + direction, col - 1))
            moves.append((row + direction, col + 1))

        return moves
