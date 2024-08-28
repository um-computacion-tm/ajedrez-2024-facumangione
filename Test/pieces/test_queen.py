import unittest
from game.pieces import Queen


class TestQueen(unittest.TestCase):
    def test_basic_queen_moves(self):
        queen = Queen("black")
        self.assertEqual(queen.color, "black")

        start_row, start_col = 4, 4
        rook_moves = [(i, 4) for i in range(8) if i != 4] + [(4, i) for i in range(8) if i != 4]
        bishop_moves = [(r, c) for r, c in [
            (3, 3), (2, 2), (1, 1), (0, 0),  # Diagonal superior izquierda
            (3, 5), (2, 6), (1, 7),          # Diagonal superior derecha
            (5, 3), (6, 2), (7, 1),          # Diagonal inferior izquierda
            (5, 5), (6, 6), (7, 7)           # Diagonal inferior derecha
        ]]
        expected_moves = rook_moves + bishop_moves

        self.assertEqual(set(queen.basic_queen_moves(start_row, start_col)), set(expected_moves))
if __name__ == '__main__':
    unittest.main()