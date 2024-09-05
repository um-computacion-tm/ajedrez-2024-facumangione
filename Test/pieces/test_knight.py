import unittest
from game.pieces import Knight
from game.board import Board

class TestKnight(unittest.TestCase):

    def test_str(self):
        knight = Knight("WHITE")
        self.assertEqual(
            str(knight),
            "♘",
        )

    def test_basic_knight_moves(self):
        knight = Knight("WHITE")
        expected_moves = [(2, 1), (1, 2)]
        actual_moves = knight.basic_knight_moves(0, 0)
        self.assertEqual(actual_moves, expected_moves)

    def test_knight_moves_from_center(self):
        knight = Knight("WHITE")
        possibles = knight.basic_knight_moves(4, 4)
        expected_moves = [
            (2, 3), (2, 5), (3, 2), (3, 6), (5, 2), (5, 6), (6, 3), (6, 5)
        ]
        self.assertEqual(possibles, expected_moves)

    def test_knight_moves_out_of_bounds(self):
        knight = Knight("WHITE")
        expected_moves = [(2, 1), (1, 2)]
        self.assertEqual(knight.basic_knight_moves(0, 0), expected_moves)

if __name__ == '__main__':
    unittest.main()
