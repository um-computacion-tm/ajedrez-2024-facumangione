# test_knight.py

import unittest
from game.pieces.knight import Knight

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.knight_white = Knight("WHITE")
        self.knight_black = Knight("BLACK")

    def test_str(self):
        self.assertEqual(str(self.knight_white), "♘")
        self.assertEqual(str(self.knight_black), "♞")

    def test_basic_knight_moves_center(self):
        # El caballo en la posición central (4, 4) tiene 8 posiciones en forma de "L"
        expected_moves = [
            (6, 5), (6, 3),
            (2, 5), (2, 3),
            (5, 6), (5, 2),
            (3, 6), (3, 2)
        ]
        self.assertCountEqual(self.knight_white.basic_knight_moves(4, 4), expected_moves)

    def test_basic_knight_moves_corner(self):
        # El caballo en la esquina (0, 0) tiene 2 movimientos posibles
        expected_moves = [(2, 1), (1, 2)]
        self.assertCountEqual(self.knight_black.basic_knight_moves(0, 0), expected_moves)

    def test_basic_knight_moves_edge(self):
        # El caballo en el borde (0, 4) tiene 4 movimientos posibles
        expected_moves = [(2, 5), (2, 3), (1, 6), (1, 2)]
        self.assertCountEqual(self.knight_white.basic_knight_moves(0, 4), expected_moves)

if __name__ == '__main__':
    unittest.main()
