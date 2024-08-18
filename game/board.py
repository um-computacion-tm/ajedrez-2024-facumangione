from game.piece import Rook, Pawn, Knight

class Board:
    def __init__(self):
        # Inicializa el tablero con piezas en posiciones predeterminadas
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]

        # Posiciones iniciales de las torres (rooks)
        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
        self.__positions__[7][0] = Rook("WHITE")
        self.__positions__[7][7] = Rook("WHITE")

        # Posiciones iniciales de los peones (pawns)
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK")
            self.__positions__[6][col] = Pawn("WHITE")

        # Posiciones iniciales de los caballos (knights)
        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[7][1] = Knight("WHITE")
        self.__positions__[7][6] = Knight("WHITE")

    def get_piece(self, row, col):
        piece = self.__positions__[row][col]
        return "No piece" if piece is None else ({piece.__type__}, {piece.__color__})

    def permited_move(self, from_row, from_col, to_row, to_col):
        piece = self.__positions__[from_row][from_col]
        if piece is None:
            return False

        piece_type = piece.__type__

        if piece_type == "ROOK":
            return to_row == from_row or to_col == from_col

        if piece_type == "KNIGHT":
            row_diff = abs(from_row - to_row)
            col_diff = abs(from_col - to_col)
            return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

        return False

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.__positions__[from_row][from_col]

        if piece is None:
            print("No piece to move")
            return "No piece to move"

        if not self.permited_move(from_row, from_col, to_row, to_col):
            print("The piece cannot be moved in this position")
            return "The piece cannot be moved in this position"

        self.__positions__[to_row][to_col] = piece
        self.__positions__[from_row][from_col] = None

        print(f"Moved piece from: {from_row}, {from_col} to: {to_row}, {to_col}")

        self.show_board()

    def show_board(self):
        # Función para mostrar el estado actual del tablero (puede implementar la lógica según lo requiera)
        pass
