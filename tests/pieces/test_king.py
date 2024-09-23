# test_king.py

import unittest
from game.pieces.king import King

class TestKing(unittest.TestCase):

    def setUp(self):
        self.king_white = King("WHITE")
        self.king_black = King("BLACK")

    def test_str(self):
        self.assertEqual(str(self.king_white), "♔")
        self.assertEqual(str(self.king_black), "♚")

    def test_basic_king_moves_center(self):
        # El rey en la posición central (4, 4) puede moverse a 8 posiciones
        expected_moves = [(3, 3), (3, 4), (3, 5),
                          (4, 3),         (4, 5),
                          (5, 3), (5, 4), (5, 5)]
        self.assertCountEqual(self.king_white.basic_king_moves(4, 4), expected_moves)

    def test_basic_king_moves_corner(self):
        # El rey en la esquina (0, 0) solo puede moverse a 3 posiciones
        expected_moves = [(0, 1), (1, 0), (1, 1)]
        self.assertCountEqual(self.king_black.basic_king_moves(0, 0), expected_moves)

    def test_basic_king_moves_edge(self):
        # El rey en el borde (0, 4) puede moverse a 5 posiciones
        expected_moves = [(0, 3), (0, 5),
                          (1, 3), (1, 4), (1, 5)]
        self.assertCountEqual(self.king_white.basic_king_moves(0, 4), expected_moves)

if __name__ == '__main__':
    unittest.main()

