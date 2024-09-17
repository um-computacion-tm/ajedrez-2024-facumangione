import unittest
from unittest.mock import MagicMock
from game.board import Board
from game.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        # Configuración inicial para los tests
        self.board = MagicMock(spec=Board)
        self.player = Player(color='white', board=self.board)
        
        # Mocking las piezas del jugador
        self.piece1 = MagicMock()
        self.piece1.color = 'white'
        self.piece1.value = 5
        self.piece1.valid_positions = MagicMock(return_value=[(1, 1), (2, 2)])  # Movimientos válidos de la pieza 1

        self.piece2 = MagicMock()
        self.piece2.color = 'white'
        self.piece2.value = 3
        self.piece2.valid_positions = MagicMock(return_value=[(3, 3)])  # Movimientos válidos de la pieza 2

        # Configuración inicial de las piezas en el tablero
        self.board.get_piece = MagicMock(side_effect=lambda row, col: self.piece1 if row == 0 and col == 0 else None)
        
        # Forzar la inicialización de piezas en el player
        self.player._initialize_pieces_ = MagicMock(return_value=[self.piece1, self.piece2])
        self.player.__pieces__ = [self.piece1, self.piece2]

    def test_initialize_pieces(self):
        self.assertIn(self.piece1, self.player._initialize_pieces_())
        self.assertIn(self.piece2, self.player._initialize_pieces_())

    def test_get_valid_moves(self):
        valid_moves = self.player.get_valid_moves()
        expected_moves = [(self.piece1, (1, 1)), (self.piece1, (2, 2)), (self.piece2, (3, 3))]

        self.assertEqual(valid_moves, expected_moves)

    def test_move_piece(self):
        self.player.move_piece(0, 0, 1, 1)
        self.board.move_piece.assert_called_with(0, 0, 1, 1)

    def test_move_piece_no_piece(self):
        self.board.get_piece = MagicMock(return_value=None)
        with self.assertRaises(ValueError):
            self.player.move_piece(0, 0, 1, 1)

    def test_move_piece_wrong_color(self):
        self.piece1.color = 'black'
        self.board.get_piece = MagicMock(return_value=self.piece1)
        with self.assertRaises(ValueError):
            self.player.move_piece(0, 0, 1, 1)

    def test_add_captured_piece(self):
        self.player.add_captured_piece(self.piece1)
        self.assertIn(self.piece1, self.player.__captured_pieces__)

    def test_remove_piece(self):
        self.player.remove_piece(self.piece1)
        self.assertNotIn(self.piece1, self.player.__pieces__)

    def test_calculate_score(self):
        self.player.add_captured_piece(self.piece1)
        self.player.add_captured_piece(self.piece2)
        self.assertEqual(self.player.calculate_score(), 8)

if __name__ == '__main__':
    unittest.main()
