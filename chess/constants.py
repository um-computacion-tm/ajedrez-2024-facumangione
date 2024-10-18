# constants.py

# Direcciones para movimientos rectilíneos (como torre)
RECTILINEAR_DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Direcciones para movimientos diagonales (como alfil)
DIAGONAL_DIRECTIONS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# Combinación de movimientos de torre y alfil (para reina y rey)
QUEEN_KING_DIRECTIONS = RECTILINEAR_DIRECTIONS + DIAGONAL_DIRECTIONS
