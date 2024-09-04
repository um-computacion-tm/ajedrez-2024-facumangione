import unittest
from game.pieces import Queen, Rook, Bishop

class TestQueen(unittest.TestCase):

    def test_str(self):
        queen = Queen("WHITE")
        self.assertEqual(str(queen), "♕")

    def test_basic_queen_moves(self):
        queen = Queen("WHITE")
        rook_moves = Rook("WHITE").basic_rook_moves(0, 0)
        bishop_moves = Bishop("WHITE").basic_bishop_moves(0, 0)
        expected_moves = rook_moves + bishop_moves
        self.assertEqual(queen.basic_queen_moves(0, 0), expected_moves)

if __name__ == '__main__':
    unittest.main()
