import unittest
from game.pieces import Bishop
from game.board import Board

class TestBishop(unittest.TestCase):

    def test_str(self):
        bishop = Bishop("WHITE")
        self.assertEqual(
            str(bishop),
            "♗",
        )

    def test_basic_bishop_moves(self):
        bishop = Bishop("WHITE")
        expected_moves = [(i, i) for i in range(1, 8)] + [(i, -i) for i in range(1, 8)]
        actual_moves = bishop.basic_bishop_moves(0, 0)
        # Filtramos movimientos válidos para evitar fuera de rango
        expected_moves = [(r, c) for r, c in expected_moves if 0 <= r < 8 and 0 <= c < 8]
        self.assertEqual(actual_moves, expected_moves)

    def test_bishop_moves_from_center(self):
        bishop = Bishop("WHITE")
        possibles = bishop.basic_bishop_moves(4, 4)
        expected_moves = [
            (5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1),
            (3, 3), (2, 2), (1, 1), (0, 0), (3, 5), (2, 6), (1, 7)
        ]
        self.assertEqual(possibles, expected_moves)

if __name__ == '__main__':
    unittest.main()
