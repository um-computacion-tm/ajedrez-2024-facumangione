from game.board import Board
from game.exceptions import (
    InvalidMove,
    InvalidTurn,
    InvalidMoveNoPiece,
    InvalidMoveRookMove,
    InvalidMoveKnightMove,
    InvalidMoveBishopMove,
    InvalidMoveQueenMove,
    InvalidMoveKingMove,
    InvalidMovePawnMove,
    OutOfBoard,
    EmptyPosition
)
from game.pieces.rook import Rook
from game.pieces.knight import Knight
from game.pieces.bishop import Bishop
from game.pieces.queen import Queen
from game.pieces.king import King
from game.pieces.pawn import Pawn

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.winner = None

    def is_playing(self):
        return self.winner is None

    def move(self, from_row, from_col, to_row, to_col):
        # Verificar si las coordenadas están dentro del tablero
        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
            raise OutOfBoard()

        # Obtener la pieza de la posición inicial
        piece = self.__board__.get_piece(from_row, from_col)

        if not piece:
            raise EmptyPosition()

        # Verificar que la pieza es del color que le corresponde al turno
        if piece.color != self.__turn__:
            raise InvalidTurn(f"It is {self.__turn__}'s turn, not {piece.color}'s turn")

        # Validar que el movimiento es legal para la pieza
        if not piece.valid_positions(from_row, from_col, to_row, to_col):
            if isinstance(piece, Rook):
                raise InvalidMoveRookMove(f"Rook cannot move from ({from_row}, {from_col}) to ({to_row}, {to_col})")
            elif isinstance(piece, Knight):
                raise InvalidMoveKnightMove(f"Knight cannot move from ({from_row}, {from_col}) to ({to_row}, {to_col})")
            elif isinstance(piece, Bishop):
                raise InvalidMoveBishopMove(f"Bishop cannot move from ({from_row}, {from_col}) to ({to_row}, {to_col})")
            elif isinstance(piece, Queen):
                raise InvalidMoveQueenMove(f"Queen cannot move from ({from_row}, {from_col}) to ({to_row}, {to_col})")
            elif isinstance(piece, King):
                raise InvalidMoveKingMove(f"King cannot move from ({from_row}, {from_col}) to ({to_row}, {to_col})")
            elif isinstance(piece, Pawn):
                raise InvalidMovePawnMove(f"Pawn cannot move from ({from_row}, {from_col}) to ({to_row}, {to_col})")
            else:
                raise InvalidMove(f"Invalid move for {piece.__class__.__name__} from ({from_row}, {from_col}) to ({to_row}, {to_col})")

        # Mover la pieza y cambiar el turno
        self.__board__.move_piece(from_row, from_col, to_row, to_col)
        self.change_turn()

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
                        original_piece = self.__board__.get_piece(*move)
                        self.__board__.move_piece(row, col, move[0], move[1])
                        if not self.is_in_check(color):
                            self.__board__.move_piece(move[0], move[1], row, col)
                            self.__board__.place_piece(move[0], move[1], original_piece)
                            return False
                        self.__board__.move_piece(move[0], move[1], row, col)
                        self.__board__.place_piece(move[0], move[1], original_piece)
        return True

    def is_in_check(self, color):
        # Implementación de la lógica para verificar si el rey está en jaque
        return False

    def check_for_stalemate(self):
        if self.is_stalemate(self.turn):
            self.winner = None
