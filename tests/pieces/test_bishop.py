# test_bishop.py

import unittest
from game.pieces.bishop import Bishop

class TestBishop(unittest.TestCase):

    def setUp(self):
        self.bishop_white = Bishop("WHITE")
        self.bishop_black = Bishop("BLACK")

    def test_str(self):
        self.assertEqual(str(self.bishop_white), "♗")
        self.assertEqual(str(self.bishop_black), "♝")

    def test_basic_bishop_moves_center(self):
        # El alfil en la posición central (4, 4) tiene movimientos diagonales
        expected_moves = [
            (3, 3), (2, 2), (1, 1), (0, 0),
            (3, 5), (2, 6), (1, 7),
            (5, 3), (6, 2), (7, 1),
            (5, 5), (6, 6), (7, 7)
        ]
        self.assertCountEqual(self.bishop_white.basic_bishop_moves(4, 4), expected_moves)

    def test_basic_bishop_moves_corner(self):
        # El alfil en la esquina (0, 0) solo puede moverse en una diagonal
        expected_moves = [
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)
        ]
        self.assertCountEqual(self.bishop_black.basic_bishop_moves(0, 0), expected_moves)

    def test_basic_bishop_moves_edge(self):
        # El alfil en el borde (0, 4) puede moverse en dos diagonales
        expected_moves = [
            (1, 3), (2, 2), (3, 1), (4, 0),
            (1, 5), (2, 6), (3, 7)
        ]
        self.assertCountEqual(self.bishop_white.basic_bishop_moves(0, 4), expected_moves)

if __name__ == '__main__':
    unittest.main()
