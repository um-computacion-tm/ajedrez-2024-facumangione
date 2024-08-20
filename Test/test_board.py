import unittest
from game.board import Board 
from game.piece import Rook 

class TestBoard(unittest.TestCase):
    
    def setUp(self):
        #inicializa un nuevo tablero.
        self.board = Board()
    
    def test_initial_setup(self):
        #el tablero se inicializa correctamente
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        
        #las piezas son del color correcto
        self.assertEqual(self.board.get_piece(0, 0).color, "BLACK")
        self.assertEqual(self.board.get_piece(0, 7).color, "BLACK")
        self.assertEqual(self.board.get_piece(7, 0).color, "WHITE")
        self.assertEqual(self.board.get_piece(7, 7).color, "WHITE")
    
    def test_empty_square(self):
        #una posición vacía del tablero devuelve None
        self.assertIsNone(self.board.get_piece(4, 4))

if __name__ == "__main__":
    unittest.main()
