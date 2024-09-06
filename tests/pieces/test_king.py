import unittest
from game.pieces.king import King

class TestKing(unittest.TestCase):

    def test_str(self):
        king = King("WHITE")
        self.assertEqual(str(king), "♔")

    def test_basic_king_moves(self):
        king = King("WHITE")
        expected_moves = [(0, 1), (1, 1), (1, 0)]
        self.assertEqual(king.basic_king_moves(0, 0), expected_moves)

    def test_king_moves_out_of_bounds(self):
        king = King("WHITE")
        expected_moves = [(0, 1), (1, 1), (1, 0)]
        self.assertEqual(king.basic_king_moves(0, 0), expected_moves)

if __name__ == '__main__':
    unittest.main()
