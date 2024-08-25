class Piece:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

### TORRES ###
class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def basic_rook_moves(self, row, col):
        # Movimientos verticales y horizontales
        moves = [(r, col) for r in range(8) if r != row] + \
                [(row, c) for c in range(8) if c != col]
        return moves

### ALFILES ###
class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def basic_bishop_moves(self, row, col):
        # Movimientos diagonales
        moves = []
        for delta in range(1, 8):
            moves += [
                (row + delta, col + delta),
                (row + delta, col - delta),
                (row - delta, col + delta),
                (row - delta, col - delta)
            ]
        # Filtrar movimientos fuera del tablero
        moves = [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]
        return moves

### CABALLOS ###
class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def basic_knight_moves(self, row, col):
        # Movimientos en L
        possible_moves = [
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (2, 1), (1, 2), (-1, 2), (-2, 1)
        ]
        moves = [(row + dr, col + dc) for dr, dc in possible_moves
                 if 0 <= row + dr < 8 and 0 <= col + dc < 8]
        return moves

### REINAS ###
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def basic_queen_moves(self, row, col):
        # Movimientos de la reina (combinación de torre y alfil)
        rook_moves = Rook(self.color).basic_rook_moves(row, col)
        bishop_moves = Bishop(self.color).basic_bishop_moves(row, col)
        return rook_moves + bishop_moves

### PEONES ###
class Pawn:
    def __init__(self, color):
        self.color = color

    def basic_pawn_moves(self, row, col):
        moves = []
        if self.color == "BLACK":
            if row < 7:
                moves.append((row + 1, col))
            if row == 1:
                moves.append((row + 2, col))
        else:  # Para los peones blancos
            if row > 0:
                moves.append((row - 1, col))
            if row == 6:
                moves.append((row - 2, col))
        return moves

    
    def eat_pieces_with_peon(self, row, col):
        moves = []
        if self.color == "WHITE":
            moves = [(row - 1, col - 1), (row - 1, col + 1)]
        elif self.color == "BLACK":
            moves = [(row + 1, col - 1), (row + 1, col + 1)]
        return moves

        
###REYES###
class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def basic_king_moves(self, row, col):
        # Definir las direcciones en las que se puede mover el rey
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Movimientos diagonales superiores
            (0, -1),          (0, 1),    # Movimientos horizontales
            (1, -1), (1, 0), (1, 1)      # Movimientos diagonales inferiores
        ]

        moves = []
        for direction_r, direction_c in directions:
            r, c = row + direction_r, col + direction_c
            if 0 <= r < 8 and 0 <= c < 8:  # Asegurarse de que el movimiento esté dentro del tablero
                moves.append((r, c))

        return moves
