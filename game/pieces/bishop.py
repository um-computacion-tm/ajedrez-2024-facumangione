from piece import Piece

class Bishop(Piece):
    def __init__(self, color, board):
        super().__init__(color)
        self.__board__ = board

    def basic_bishop_moves(self, row, col):
        # Movimientos diagonales
        moves = []
        for delta in range(1, 8):
            moves += [
                (row + delta, col + delta),  # Diagonal hacia abajo a la derecha
                (row + delta, col - delta),  # Diagonal hacia abajo a la izquierda
                (row - delta, col + delta),  # Diagonal hacia arriba a la derecha
                (row - delta, col - delta)   # Diagonal hacia arriba a la izquierda
            ]
        
        # Filtrar movimientos fuera del tablero
        valid_moves = [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]
        return valid_moves

    def possible_positions(self, row, col):
        valid_positions = []
        moves = self.basic_bishop_moves(row, col)
        
        for move in moves:
            r, c = move
            piece_at_destination = self.__board__.get_piece(r, c)
            if piece_at_destination is None:
                valid_positions.append(move)  # Agregar si la casilla está vacía
            elif piece_at_destination.color != self.color:
                valid_positions.append(move)  # Agregar si la casilla tiene una pieza del oponente
                break  # No puede saltar sobre piezas
            else:
                break  # No puede moverse si hay una pieza del mismo color
        
        return valid_positions

    withe_str = "♗"
    black_str = "♝"

    def __str__(self):
        return self.withe_str if self.color == "WHITE" else self.black_str
