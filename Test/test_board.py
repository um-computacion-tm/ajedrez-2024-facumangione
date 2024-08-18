import unittest
from unittest.mock import patch, Mock
from io import StringIO

# Importar clases del módulo de ajedrez
from game.piece import Piece, Rook, Pawn
from game.board import Board
from game.chess import Chess

# Clase para probar la funcionalidad del juego de ajedrez
class TestChess(unittest.TestCase):
    
    def setUp(self):
        self.chess = Chess()

    def test_initial_turn(self):
        expected_turn = "WHITE"
        self.assertEqual(self.chess.__turn__, expected_turn)

    def test_turn_switching(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.__turn__, "BLACK")
        self.chess.change_turn()
        self.assertEqual(self.chess.__turn__, "WHITE")

    @patch('builtins.print')
    def test_piece_movement(self, mock_print):
        start_row, start_col, end_row, end_col = 7, 0, 6, 0
        self.chess.move(start_row, start_col, end_row, end_col)
        
        self.assertIsNone(self.chess.__board__.get_piece(start_row, start_col))
        self.assertEqual(self.chess.__turn__, "WHITE")

    @patch('builtins.print')
    def test_invalid_move_no_piece(self, mock_print):
        non_existing_piece = self.chess.__board__.get_piece(7, 0)
        
        self.assertEqual(self.chess.move(5, 7, 2, 2), "You can't move a piece that doesn't exist")


# Clase para probar la funcionalidad del tablero de ajedrez
class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initial_board_setup(self):
        rook_type = "ROOK"
        self.assertEqual(self.board.__positions__[0][0].__type__, rook_type)

    def test_empty_position(self):
        empty_position = (3, 3)
        self.assertIsNone(self.board.get_piece(*empty_position))

    @patch('builtins.print')
    def test_piece_movement(self, mock_print):
        start_row, start_col, end_row, end_col = 0, 0, 0, 1
        self.board.move_piece(start_row, start_col, end_row, end_col)
        
        self.assertEqual(self.board.get_piece(end_row, end_col), ({'ROOK'}, {'BLACK'}))
        self.assertIsNone(self.board.get_piece(start_row, start_col))

    @patch('builtins.print')
    def test_invalid_move_no_piece(self, mock_print):
        empty_pos_start, empty_pos_end = (3, 3), (4, 4)
        
        self.assertEqual(self.board.move_piece(*empty_pos_start, *empty_pos_end), "No piece to move")
        self.assertIsNone(self.board.get_piece(*empty_pos_start))
        self.assertIsNone(self.board.get_piece(*empty_pos_end))

    def test_knight_valid_moves(self):
        knight_pos, valid_move_1, valid_move_2 = (0, 1), (2, 2), (2, 0)
        
        self.assertTrue(self.board.permited_move(*knight_pos, *valid_move_1))
        self.assertTrue(self.board.permited_move(*knight_pos, *valid_move_2))

    def test_rook_invalid_move(self):
        rook_pos, invalid_move = (0, 0), (3, 2)
        
        self.assertFalse(self.board.permited_move(*rook_pos, *invalid_move))


# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
