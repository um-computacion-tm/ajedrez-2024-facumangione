import unittest
from game.pieces.rook import Rook
from game.pieces.knight import Knight
from game.pieces.bishop import Bishop
from game.pieces.queen import Queen
from game.pieces.king import King
from game.pieces.pawn import Pawn
from game.board import Board
from game.chess import Chess
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

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()

    def test_initial_setup(self):
        # Verificar que la posición inicial del tablero es correcta (similar a lo que ya se había hecho)
        board = self.chess.show_board()
        self.assertIn("♖", board)  # Verifica que la torre blanca está en el tablero
        self.assertIn("♜", board)  # Verifica que la torre negra está en el tablero

    def test_valid_move(self):
        # Mover un peón blanco (movimiento válido)
        self.chess.move(6, 0, 5, 0)  # Mueve el peón blanco de la posición (6,0) a (5,0)
        self.assertIsNone(self.chess.__board__.get_piece(6, 0))  # El peón ya no está en su posición original
        self.assertIsInstance(self.chess.__board__.get_piece(5, 0), Pawn)  # El peón está en la nueva posición

    def test_invalid_move_no_piece(self):
        # Intentar mover una pieza desde una posición vacía
        with self.assertRaises(EmptyPosition):
            self.chess.move(3, 3, 4, 4)  # Posición vacía en la posición (3,3)

    def test_invalid_turn(self):
        # Intentar mover una pieza en el turno incorrecto
        with self.assertRaises(InvalidTurn):
            self.chess.move(1, 0, 2, 0)  # Intentar mover un peón negro en el turno de las blancas

    def test_invalid_move_out_of_board(self):
        # Intentar mover una pieza fuera del tablero
        with self.assertRaises(OutOfBoard):
            self.chess.move(0, 0, -1, 0)  # Movimiento fuera del tablero (posición negativa)

    def test_invalid_move_piece(self):
        # Intentar un movimiento inválido con una pieza (torre moviéndose diagonalmente)
        self.chess.move(6, 0, 5, 0)  # Mueve un peón blanco para liberar la torre
        with self.assertRaises(InvalidMoveRookMove):
            self.chess.move(7, 0, 6, 1)  # Intentar mover la torre blanca diagonalmente (movimiento inválido)

    def test_change_turn(self):
        # Verificar que el turno cambia después de un movimiento válido
        self.assertEqual(self.chess.turn, "WHITE")
        self.chess.move(6, 0, 5, 0)  # Mover el peón blanco
        self.assertEqual(self.chess.turn, "BLACK")  # Después del movimiento, debe ser turno de las negras

    def test_check_for_stalemate(self):
        # Simular una situación de tablas (stalemate)
        self.chess.__board__.clear()  # Limpiar el tablero para simular una situación de tablas
        self.chess.__board__.place_piece(7, 7, King("BLACK"))
        self.chess.__board__.place_piece(0, 0, King("WHITE"))
        self.chess.__board__.place_piece(6, 6, Queen("WHITE"))
        
        # Simular turno de negras donde no tienen movimientos legales
        self.chess.change_turn()
        self.assertTrue(self.chess.is_stalemate("BLACK"))

    def test_stalemate_winner(self):
        # Verificar que después de un stalemate no hay ganador
        self.chess.__board__.clear()  # Limpiar el tablero para simular tablas
        self.chess.__board__.place_piece(7, 7, King("BLACK"))
        self.chess.__board__.place_piece(0, 0, King("WHITE"))
        self.chess.__board__.place_piece(6, 6, Queen("WHITE"))

        # Simular que las negras están en tablas
        self.chess.change_turn()
        self.chess.check_for_stalemate()
        self.assertIsNone(self.chess.winner)

if __name__ == '__main__':
    unittest.main()
