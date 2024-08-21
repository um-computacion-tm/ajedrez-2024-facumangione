import unittest
from game.piece import Rook, Bishop, Knight, Queen, Pawn, King
class TestRook(unittest.TestCase):
    def test_basic_rook_moves(self):
        rook = Rook("blanco")
        self.assertEqual(rook.color, "blanco")
        expected_moves = [(i, 0) for i in range(8) if i != 0] + [(0, i) for i in range(8) if i != 0]
        self.assertEqual(rook.basic_rook_moves(0, 0), expected_moves)

class TestBishop(unittest.TestCase):
    def test_basic_bishop_moves(self):
        bishop = Bishop("blanco")
        self.assertEqual(bishop.color, "blanco")

        expected_moves = [
            [(2, 2), (1, 1), (0, 0)],  # Diagonal superior izquierda
            [(2, 4), (1, 5), (0, 6)],  # Diagonal superior derecha
            [(4, 2), (5, 1), (6, 0)],  # Diagonal inferior izquierda
            [(4, 4), (5, 5), (6, 6), (7, 7)]  # Diagonal inferior derecha
        ]

        # Testear las cuatro direcciones diagonales
        self.assertEqual(Bishop("blanco").basic_bishop_moves(3, 3), sum(expected_moves, []))

class TestKnight(unittest.TestCase):
    def test_basic_knight_moves(self):
        knight = Knight("blanco")
        self.assertEqual(knight.color, "blanco")

        start_row, start_col = 4, 4
        expected_moves = [(2, 3), (3, 2), (5, 2), (6, 3), (6, 5), (5, 6), (3, 6), (2, 5)]

        self.assertEqual(set(knight.basic_knight_moves(start_row, start_col)), set(expected_moves))

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

class TestPawn(unittest.TestCase):
    def test_basic_pawn_moves(self):
        pawn_black = Pawn("BLACK")
        pawn_white = Pawn("WHITE")
        self.assertEqual(pawn_black.color, "BLACK")
        self.assertEqual(pawn_white.color, "WHITE")

        expected_moves_black = [(0, -1), (0, -2), (-1, -1), (1, -1)]
        expected_moves_white = [(0, 1), (0, 2), (-1, 1), (1, 1)]

        self.assertEqual(pawn_black.basic_pawn_moves(0, 0), expected_moves_black)
        self.assertEqual(pawn_white.basic_pawn_moves(0, 0), expected_moves_white)

    def test_eat_pieces_with_pawn(self):
        test_cases = [
            ("BLACK", [(7, 0), (7, 2)], 6, 1),
            ("WHITE", [(5, 0), (5, 2)], 6, 1)
        ]
        
        for color, expected_moves, start_row, start_col in test_cases:
            pawn = Pawn(color)
            self.assertEqual(set(pawn.eat_pieces_with_peon(start_row, start_col)), set(expected_moves))
            

class TestKing(unittest.TestCase):
    def test_basic_king_moves(self):
        king = King("black")
        self.assertEqual(king.color, "black")

        start_row, start_col = 4, 4

        # Movimientos esperados del rey (una casilla en cualquier dirección)
        expected_moves = [
            (3, 3), (3, 4), (3, 5),  # Superior
            (4, 3),         (4, 5),  # Lados
            (5, 3), (5, 4), (5, 5)   # Inferior
        ]

        self.assertEqual(set(king.basic_king_moves(start_row, start_col)), set(expected_moves))

if __name__ == '__main__':
    unittest.main()
