from game.board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.winner = None

    def is_playing(self):
        return True

    def move(self, from_row, from_col, to_row, to_col):
        # Obtener la pieza de la posición inicial
        piece = self.__board__.get_piece(from_row, from_col)
        
        # Validar que la pieza existe y que es del color correcto
        if piece is None or piece.color != self.__turn__:
            print("No valid piece to move")
            return False

        # Validar que el movimiento es legal
        if not self.is_valid_move(from_row, from_col, to_row, to_col):
            print("Invalid move")
            return False

        # Mover la pieza y cambiar el turno
        self.__board__.move_piece(from_row, from_col, to_row, to_col)
        self.change_turn()
        return True

    def is_valid_move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if piece:
            return piece.valid_positions(from_row, from_col, to_row, to_col)
        return False

    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

    def is_stalemate(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.__board__.get_piece(row, col)
                if piece and piece.color == color:
                    for move in piece.get_valid_moves(self.__board__, row, col):
                        # Simular el movimiento
                        original_piece = self.__board__.get_piece(*move)
                        self.__board__.move_piece(row, col, move[0], move[1])
                        if not self.is_in_check(color):
                            # Deshacer el movimiento
                            self.__board__.move_piece(move[0], move[1], row, col)
                            self.__board__.place_piece(move[0], move[1], original_piece)
                            return False
                        # Deshacer el movimiento
                        self.__board__.move_piece(move[0], move[1], row, col)
                        self.__board__.place_piece(move[0], move[1], original_piece)
        return True

    def is_in_check(self, color):
        # Implementar lógica para verificar si el rey del color dado está en jaque
        return False  # Simplificación

    def check_for_stalemate(self):
        if self.is_stalemate(self.turn):
            self.winner = None
