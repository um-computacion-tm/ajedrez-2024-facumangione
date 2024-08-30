class InvalidMove(Exception):
    """Clase base para excepciones de movimientos inválidos en ajedrez."""
    pass

class InvalidMoveNoPiece(InvalidMove):
    """Excepción para movimientos cuando no hay una pieza en la posición de origen."""
    def __init__(self, from_row, from_col):
        self.from_row = from_row
        self.from_col = from_col
        super().__init__(f"No piece found at position ({from_row}, {from_col})")

class InvalidMoveRookMove(InvalidMove):
    """Excepción para movimientos inválidos específicos de la torre."""
    def __init__(self, from_row, from_col, to_row, to_col):
        self.from_row = from_row
        self.from_col = from_col
        self.to_row = to_row
        self.to_col = to_col
        super().__init__(f"Invalid move for Rook from ({from_row}, {from_col}) to ({to_row}, {to_col})")
