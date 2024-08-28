import unittest
from game.pieces import Knight

class TestKnight(unittest.TestCase):
    def test_basic_knight_moves(self):
        knight = Knight("blanco")
        self.assertEqual(knight.color, "blanco")

        start_row, start_col = 4, 4
        expected_moves = [(2, 3), (3, 2), (5, 2), (6, 3), (6, 5), (5, 6), (3, 6), (2, 5)]

        self.assertEqual(set(knight.basic_knight_moves(start_row, start_col)), set(expected_moves))
