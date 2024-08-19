import unittest
from unittest.mock import patch, MagicMock
from game.chess import Chess
from game.board import Board

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()

    @patch.object(Board, 'get_piece', return_value="ROOK")
    @patch.object(Board, 'move_piece')
    def test_move_valid_piece(self, mock_move_piece, mock_get_piece):
        # Prueba que un movimiento válido cambia de turno y mueve la pieza
        self.chess.move(0, 0, 0, 1)

        mock_get_piece.assert_called_once_with(0, 0)
        mock_move_piece.assert_called_once_with(0, 0, 0, 1)
        self.assertEqual(self.chess.__turn__, "BLACK")

    @patch.object(Board, 'get_piece', return_value="No piece")
    def test_move_no_piece(self, mock_get_piece):
        # Prueba que no se puede mover una pieza inexistente y no cambia de turno
        message = self.chess.move(0, 0, 0, 1)

        mock_get_piece.assert_called_once_with(0, 0)
        self.assertEqual(message, "You can't move a piece that doesn't exist")
        self.assertEqual(self.chess.__turn__, "WHITE")

    def test_change_turn(self):
        # Prueba el cambio de turno
        self.chess.change_turn()
        self.assertEqual(self.chess.__turn__, "BLACK")
        self.chess.change_turn()
        self.assertEqual(self.chess.__turn__, "WHITE")

if __name__ == '__main__':
    unittest.main()
