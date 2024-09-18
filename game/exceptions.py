class InvalidMove(Exception):
    def __init__(self, message="Movimiento de pieza inválido", position=None):
        self.message = message
        self.position = position  # Posición involucrada en el error
        super().__init__(self.message)

    def __str__(self):
        if self.position:
            return f"{self.message} en la posición {self.position}"
        return self.message


class InvalidTurn(InvalidMove):
    def __init__(self, position=None):
        super().__init__(message="No puedes mover la pieza del oponente", position=position)


class EmptyPosition(InvalidMove):
    def __init__(self, position=None):
        super().__init__(message="La posición seleccionada está vacía", position=position)


class OutOfBoard(InvalidMove):
    def __init__(self, position=None):
        super().__init__(message="La posición indicada está fuera del tablero", position=position)


# Excepciones específicas de piezas
class InvalidRookMove(InvalidMove):
    def __init__(self, position=None):
        super().__init__(message="Movimiento inválido de la Torre", position=position)


class InvalidKnightMove(InvalidMove):
    def __init__(self, position=None):
        super().__init__(message="Movimiento inválido del Caballo", position=position)


class InvalidBishopMove(InvalidMove):
    def __init__(self, position=None):
        super().__init__(message="Movimiento inválido del Alfil", position=position)


class InvalidQueenMove(InvalidMove):
    def __init__(self, position=None):
        super().__init__(message="Movimiento inválido de la Reina", position=position)


class InvalidKingMove(InvalidMove):
    def __init__(self, position=None):
        super().__init__(message="Movimiento inválido del Rey", position=position)
