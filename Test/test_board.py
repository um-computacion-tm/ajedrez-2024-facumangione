import unittest
from game.pieces.piece import Rook, Knight, Bishop, Queen, King, Pawn
from game.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_setup(self):
        # Verificar las piezas negras
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertEqual(self.board.get_piece(0, 0).color, "BLACK")

        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertEqual(self.board.get_piece(0, 7).color, "BLACK")

        self.assertIsInstance(self.board.get_piece(0, 1), Knight)
        self.assertEqual(self.board.get_piece(0, 1).color, "BLACK")

        self.assertIsInstance(self.board.get_piece(0, 6), Knight)
        self.assertEqual(self.board.get_piece(0, 6).color, "BLACK")

        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
        self.assertEqual(self.board.get_piece(0, 2).color, "BLACK")

        self.assertIsInstance(self.board.get_piece(0, 5), Bishop)
        self.assertEqual(self.board.get_piece(0, 5).color, "BLACK")

        self.assertIsInstance(self.board.get_piece(0, 3), Queen)
        self.assertEqual(self.board.get_piece(0, 3).color, "BLACK")

        self.assertIsInstance(self.board.get_piece(0, 4), King)
        self.assertEqual(self.board.get_piece(0, 4).color, "BLACK")

        for i in range(8):
            self.assertIsInstance(self.board.get_piece(1, i), Pawn)
            self.assertEqual(self.board.get_piece(1, i).color, "BLACK")

        # Verificar las piezas blancas
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertEqual(self.board.get_piece(7, 0).color, "WHITE")

        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        self.assertEqual(self.board.get_piece(7, 7).color, "WHITE")

        self.assertIsInstance(self.board.get_piece(7, 1), Knight)
        self.assertEqual(self.board.get_piece(7, 1).color, "WHITE")

        self.assertIsInstance(self.board.get_piece(7, 6), Knight)
        self.assertEqual(self.board.get_piece(7, 6).color, "WHITE")

        self.assertIsInstance(self.board.get_piece(7, 2), Bishop)
        self.assertEqual(self.board.get_piece(7, 2).color, "WHITE")

        self.assertIsInstance(self.board.get_piece(7, 5), Bishop)
        self.assertEqual(self.board.get_piece(7, 5).color, "WHITE")

        self.assertIsInstance(self.board.get_piece(7, 3), Queen)
        self.assertEqual(self.board.get_piece(7, 3).color, "WHITE")

        self.assertIsInstance(self.board.get_piece(7, 4), King)
        self.assertEqual(self.board.get_piece(7, 4).color, "WHITE")

        for i in range(8):
            self.assertIsInstance(self.board.get_piece(6, i), Pawn)
            self.assertEqual(self.board.get_piece(6, i).color, "WHITE")

    def test_empty_squares(self):
        # Verificar que las posiciones vacías no tengan piezas
        for row in range(2, 6):
            for col in range(8):
                self.assertIsNone(self.board.get_piece(row, col))

    def test_str_board(self):
        board = Board(for_test=True)
        self.assertEqual(
            str(board),
            (
                "♖      ♖\n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "♜      ♜\n"
            )
        )

if __name__ == '__main__':
    unittest.main()
