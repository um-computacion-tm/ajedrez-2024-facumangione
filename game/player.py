class Player:
    def __init__(self, color, board):
        self.__color__ = color  # Almacena el color del jugador
        self.__board__ = board  # Almacena la instancia del tablero
        self.__pieces__ = self._initialize_pieces_()  # Almacena las piezas que moverá cada jugador
        self.__captured_pieces__ = []  # Almacena las piezas capturadas

    def _initialize_pieces_(self):  # Recorre el board y almacena las piezas que pertenecen al jugador
        pieces = []
        for row in range(8):
            for col in range(8):
                piece = self.__board__.get_piece(row, col)
                if piece and piece.color == self.__color__:
                    pieces.append(piece)
        return pieces

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        
        if piece is None:
            raise ValueError("No piece at the given position")
        
        if piece.color != self.__color__:
            raise ValueError("You cannot move the opponent's piece")
        
        self.__board__.move_piece(from_row, from_col, to_row, to_col)

    def add_piece(self, piece):
        self.__pieces__.append(piece)

    def add_captured_piece(self, piece):
        self.__captured_pieces__.append(piece)

    def remove_piece(self, piece):
        self.__pieces__.remove(piece)

    def calculate_score(self):
        score = 0
        for piece in self.__captured_pieces__:
            score += piece.value  # Asume que cada pieza tiene un atributo 'value'
        return score

    # Nuevo método para obtener los movimientos válidos de todas las piezas del jugador
    def get_valid_moves(self):
        valid_moves = []
        for piece in self.__pieces__:
            for row in range(8):
                for col in range(8):
                    # Verificamos si la pieza tiene una posición válida para moverse
                    for move in piece.valid_positions(self.__board__, row, col):
                        valid_moves.append((piece, move))
        return valid_moves
