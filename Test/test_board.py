import unittest
from game.board import Board
from game.piece import Rook, Pawn, Knight

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board_initialization(self):
        # Verifica si las posiciones iniciales tienen las piezas correctas
        self.assertEqual(self.board.get_piece(0, 0), ({'ROOK'}, {'BLACK'}))
        self.assertEqual(self.board.get_piece(7, 7), ({'ROOK'}, {'WHITE'}))
        self.assertEqual(self.board.get_piece(1, 0), ({'PAWN'}, {'BLACK'}))
        self.assertEqual(self.board.get_piece(6, 0), ({'PAWN'}, {'WHITE'}))
        self.assertEqual(self.board.get_piece(0, 1), ({'KNIGHT'}, {'BLACK'}))
        self.assertEqual(self.board.get_piece(7, 6), ({'KNIGHT'}, {'WHITE'}))

    def test_get_piece_empty(self):
        # Verifica si obtener una pieza de una posición vacía devuelve "No piece"
        self.assertEqual(self.board.get_piece(3, 3), "No piece")

    def test_move_piece(self):
        # Mueve una pieza y verifica las posiciones antes y después del movimiento
        self.board.move_piece(0, 0, 0, 1)
        self.assertEqual(self.board.get_piece(0, 1), ({'ROOK'}, {'BLACK'}))
        self.assertEqual(self.board.get_piece(0, 0), "No piece")

    def test_move_piece_no_piece(self):
        # Intenta mover una pieza desde una posición vacía y verifica el comportamiento
        result = self.board.move_piece(3, 3, 4, 4)
        self.assertEqual(result, "No piece to move")
        self.assertEqual(self.board.get_piece(3, 3), "No piece")
        self.assertEqual(self.board.get_piece(4, 4), "No piece")

    def test_permited_move_rook(self):
        # Verifica los movimientos permitidos para la torre
        self.assertTrue(self.board.permited_move(0, 0, 0, 5))  # Movimiento horizontal permitido
        self.assertTrue(self.board.permited_move(0, 0, 3, 0))  # Movimiento vertical permitido
        self.assertFalse(self.board.permited_move(0, 0, 3, 2))  # Movimiento diagonal no permitido

if __name__ == '__main__':
    unittest.main()

