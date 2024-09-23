# test_queen.py

import unittest
from game.pieces.queen import Queen

class TestQueen(unittest.TestCase):

    def setUp(self):
        self.queen_white = Queen("WHITE")
        self.queen_black = Queen("BLACK")

    def test_str(self):
        self.assertEqual(str(self.queen_white), "♕")
        self.assertEqual(str(self.queen_black), "♛")

    def test_basic_queen_moves_center(self):
        # La reina en la posición central (4, 4) tiene movimientos combinados de torre y alfil
        expected_moves = [
            # Horizontales y verticales
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7),
            (0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (6, 4), (7, 4),
            # Diagonales
            (3, 3), (2, 2), (1, 1), (0, 0),
            (3, 5), (2, 6), (1, 7),
            (5, 3), (6, 2), (7, 1),
            (5, 5), (6, 6), (7, 7)
        ]
        self.assertCountEqual(self.queen_white.basic_queen_moves(4, 4), expected_moves)

    def test_basic_queen_moves_corner(self):
        # La reina en la esquina (0, 0) puede moverse a 14 posiciones
        expected_moves = [
            # Horizontales y verticales
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            # Diagonales
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)
        ]
        self.assertCountEqual(self.queen_black.basic_queen_moves(0, 0), expected_moves)

    def test_basic_queen_moves_edge(self):
        # La reina en el borde (0, 4) tiene 14 movimientos
        expected_moves = [
            # Horizontales y verticales
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 5), (0, 6), (0, 7),
            (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),
            # Diagonales
            (1, 3), (2, 2), (3, 1), (4, 0),
            (1, 5), (2, 6), (3, 7)
        ]
        self.assertCountEqual(self.queen_white.basic_queen_moves(0, 4), expected_moves)

if __name__ == '__main__':
    unittest.main()
