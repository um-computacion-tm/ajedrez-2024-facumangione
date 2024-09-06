import unittest
from game.pieces.pawn import Pawn

class TestPawn(unittest.TestCase):

    def test_str(self):
        pawn = Pawn("WHITE")
        self.assertEqual(str(pawn), "♙")

    def test_basic_pawn_moves(self):
        pawn = Pawn("WHITE")
        expected_moves = [(5, 4), (4, 4)]
        self.assertEqual(pawn.basic_pawn_moves(6, 4), expected_moves)

    def test_eat_pieces_with_pawn(self):
        pawn = Pawn("WHITE")
        expected_moves = [(5, 3), (5, 5)]
        self.assertEqual(pawn.eat_pieces_with_peon(6, 4), expected_moves)

if __name__ == '__main__':
    unittest.main()
