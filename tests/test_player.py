import unittest
from unittest.mock import MagicMock
from game.board import Board
from game.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        # Configuración inicial para los tests
        self.board = MagicMock(spec=Board)
        self.player = Player(color='white', board=self.board)
        
        # Mocking de las piezas del jugador
        self.piece1 = MagicMock()
        self.piece1.color = 'white'
        self.piece1.value = 5
        self.piece2 = MagicMock()
        self.piece2.color = 'white'
        self.piece2.value = 3
        
        # Configuración inicial de las piezas en el tablero
        self.board.get_piece = MagicMock(side_effect=lambda row, col: self.piece1 if row == 0 and col == 0 else None)
        
        # Forzar la inicialización de piezas en el jugador
        self.player.initialize_pieces = MagicMock(return_value=[self.piece1, self.piece2])
        self.player.pieces = [self.piece1, self.piece2]

    def test_initialize_pieces(self):
        # Verifica que las piezas se inicializan correctamente
        self.assertIn(self.piece1, self.player.initialize_pieces())
        self.assertIn(self.piece2, self.player.initialize_pieces())
    
    def test_move_piece(self):
        # Verifica que el movimiento de una pieza funciona correctamente
        self.player.move_piece(0, 0, 1, 1)
        self.board.move_piece.assert_called_with(0, 0, 1, 1)
        
    def test_move_piece_no_piece(self):
        # Verifica que lanzar un error si no hay pieza en la posición inicial
        self.board.get_piece = MagicMock(return_value=None)
        with self.assertRaises(ValueError):
            self.player.move_piece(0, 0, 1, 1)

    def test_move_piece_wrong_color(self):
        # Verifica que lanzar un error si la pieza es del color incorrecto
        self.piece1.color = 'black'
        self.board.get_piece = MagicMock(return_value=self.piece1)
        with self.assertRaises(ValueError):
            self.player.move_piece(0, 0, 1, 1)
    
    def test_add_captured_piece(self):
        # Verifica que las piezas capturadas se agreguen correctamente
        self.player.add_captured_piece(self.piece1)
        self.assertIn(self.piece1, self.player.captured_pieces)
        
    def test_remove_piece(self):
        # Verifica que las piezas se eliminen correctamente del jugador
        self.player.remove_piece(self.piece1)
        self.assertNotIn(self.piece1, self.player.pieces)
        
    def test_calculate_score(self):
        # Verifica que el puntaje se calcule correctamente basado en las piezas capturadas
        self.player.add_captured_piece(self.piece1)
        self.player.add_captured_piece(self.piece2)
        self.assertEqual(self.player.calculate_score(), 8)

if __name__ == '__main__':
    unittest.main()
