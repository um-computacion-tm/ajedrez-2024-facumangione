from game.board import Board

class Player:
    def __init__(self, color, board):
        self.color = color  # Almacena el color del jugador
        self.board = board  # Almacena la instancia del tablero
        self.pieces = self.initialize_pieces()  # Almacena las piezas que moverá cada jugador
        self.captured_pieces = []  # Almacena las piezas capturadas

    def initialize_pieces(self):
        # Recorre el tablero y almacena las piezas que pertenecen al jugador
        pieces = []
        for row in range(8):
            for col in range(8):
                piece = self.board.get_piece(row, col)
                if piece and piece.color == self.color:
                    pieces.append(piece)
        return pieces

    def move_piece(self, from_row, from_col, to_row, to_col):
        # Mueve una pieza si pertenece al jugador
        piece = self.board.get_piece(from_row, from_col)

        if piece is None:
            raise ValueError("No piece at the given position")
        
        if piece.color != self.color:
            raise ValueError("You cannot move the opponent's piece")
        
        self.board.move_piece(from_row, from_col, to_row, to_col)

    def add_piece(self, piece):
        # Agrega una pieza al jugador (por ejemplo, si un peón llega al final)
        self.pieces.append(piece)

    def add_captured_piece(self, piece):
        # Agrega una pieza capturada al registro
        self.captured_pieces.append(piece)

    def remove_piece(self, piece):
        # Elimina una pieza del jugador (cuando es capturada)
        self.pieces.remove(piece)

    def calculate_score(self):
        # Calcula el puntaje basado en las piezas capturadas
        score = sum(piece.value for piece in self.captured_pieces)  # Asume que cada pieza tiene un atributo 'value'
        return score
