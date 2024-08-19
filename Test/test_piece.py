import unittest
from game.piece import Piece, Rook, Pawn

class TestPiece(unittest.TestCase):
    def test_piece_initialization(self):
        piece = Piece("WHITE")
        self.assertEqual(piece.get_color(), "WHITE")
        self.assertIsNone(piece.get_type())
    def test_pawn_initialization(self):
        pawn = Pawn("WHITE")
        self.assertEqual(pawn.get_color(), "WHITE")
        self.assertEqual(pawn.get_type(), "PAWN")
        
class TestRook(unittest.TestCase):
    def setUp(self):
        self.rook_black = Rook("BLACK")
        self.rook_white = Rook("WHITE")

    def test_rook_initialization(self):
        # Verifica que la torre se inicializa correctamente con el color adecuado
        self.assertEqual(self.rook_black.get_color(), "BLACK", "La torre debe ser negra")
        self.assertEqual(self.rook_white.get_color(), "WHITE", "La torre debe ser blanca")
        
    def test_rook_movimientos_basicos(self):
        # Verifica los movimientos básicos de la torre desde la posición (0, 0)
        expected_moves = [(r, 0) for r in range(1, 8)] + [(0, c) for c in range(1, 8)]
        actual_moves = self.rook_black.movimientos_basicos_de_torres(0, 0)

        self.assertEqual(len(actual_moves), len(expected_moves), "Debe haber 14 movimientos posibles")
        self.assertListEqual(sorted(actual_moves), sorted(expected_moves), "Los movimientos no coinciden con los esperados")

    def test_rook_no_self_position_in_moves(self):
        # Verifica que la posición actual no esté incluida en los movimientos posibles
        moves = self.rook_black.movimientos_basicos_de_torres(0, 0)
        self.assertNotIn((0, 0), moves, "La posición actual no debe estar en los movimientos posibles")


if __name__ == '__main__':
    unittest.main()
