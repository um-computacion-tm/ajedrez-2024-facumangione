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
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
