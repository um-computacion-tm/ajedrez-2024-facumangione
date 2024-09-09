import unittest
from game.board import Board
from game.chess import Chess
from game.exceptions import InvalidMove, InvalidMoveNoPiece, InvalidMoveRookMove, OutOfBoard, InvalidMoveBishopMove, InvalidMoveKnightMove

class TestChess(unittest.TestCase):
    def setUp(self):
        # Inicializa un nuevo tablero
        self.board = Board()

    def test_initial_turn(self):
        chess_game = Chess()  # Nueva partida
        self.assertEqual(chess_game.turn, "WHITE")  # Verifico que el 1er turno sea del blanco

    def test_turn_change_correctly(self):
        chess_game = Chess()  # Nueva partida
        self.assertEqual(chess_game.turn, "WHITE")  # Verifico que el 1er turno sea del blanco

        # Debo de realizar un movimiento como 2do paso
        chess_game.move(1, 0, 2, 0)  # Mover un peón desde (1, 0) a (2, 0)
        "(fila origen, columna origen, fila destino, columna destino)"

        # Verifico el cambio de turno (que es lo que busco)
        self.assertEqual(chess_game.turn, "BLACK")

    def test_turn_does_not_change_on_invalid_move(self):
        chess_game = Chess()
        with self.assertRaises(InvalidMoveNoPiece):
            chess_game.move(4, 4, 5, 5)  # Movimiento sin pieza en la posición de origen
        self.assertEqual(chess_game.turn, "WHITE")  # El turno no debería cambiar

    def test_piece_capture(self):
        chess_game = Chess()
        chess_game.move(6, 4, 4, 4)  # Mover peón blanco
        chess_game.move(1, 3, 3, 3)  # Mover peón negro
        chess_game.move(4, 4, 3, 3)  # Captura el peón negro
        
        self.assertIsNone(chess_game.__board__.get_piece(4, 4))  # Verificar que la posición original está vacía
        self.assertIsNotNone(chess_game.__board__.get_piece(3, 3))  # Verificar que el peón blanco ocupa la posición del peón negro
        self.assertEqual(chess_game.__board__.get_piece(3, 3).color, "WHITE")  # Verificar que la pieza capturada es blanca

    def test_invalid_piece_movement(self):
        chess_game = Chess()
        with self.assertRaises(InvalidMoveRookMove):
            chess_game.move(0, 0, 3, 0)  # Intentar mover una torre desde (0, 0) a (3, 0), lo cual es inválido al inicio
        self.assertIsNotNone(chess_game.__board__.get_piece(0, 0))  # Verificar que la torre sigue en su lugar original
        self.assertIsNone(chess_game.__board__.get_piece(3, 0))  # Verificar que la posición destino está vacía
        self.assertEqual(chess_game.turn, "WHITE")  # Verificar que el turno no cambió

    def test_knight_movement(self):
        chess_game = Chess()
        chess_game.move(7, 1, 5, 2)  # Mover el caballo blanco desde (7, 1) a (5, 2), un movimiento en L
        self.assertIsNone(chess_game.__board__.get_piece(7, 1))  # Verificar que la posición inicial está vacía
        self.assertIsNotNone(chess_game.__board__.get_piece(5, 2))  # Verificar que el caballo está en la nueva posición
        self.assertEqual(chess_game.__board__.get_piece(5, 2).color, "WHITE")  # Verificar que la pieza es blanca

    def test_invalid_knight_movement(self):
        chess_game = Chess()
        with self.assertRaises(InvalidMoveKnightMove):
            chess_game.move(7, 1, 6, 1)  # Intentar mover un caballo de manera inválida
        self.assertIsNotNone(chess_game.__board__.get_piece(7, 1))  # Verificar que el caballo sigue en su posición inicial

    def test_bishop_movement(self):
        chess_game = Chess()
        chess_game.move(6, 3, 4, 3)  # Mover peón para liberar al alfil
        chess_game.move(7, 2, 5, 4)  # Mover el alfil blanco en diagonal
        self.assertIsNone(chess_game.__board__.get_piece(7, 2))  # Verificar que la posición inicial está vacía
        self.assertIsNotNone(chess_game.__board__.get_piece(5, 4))  # Verificar que el alfil está en la nueva posición
        self.assertEqual(chess_game.__board__.get_piece(5, 4).color, "WHITE")  # Verificar que la pieza es blanca

    def test_invalid_bishop_movement(self):
        chess_game = Chess()
        with self.assertRaises(InvalidMoveBishopMove):
            chess_game.move(7, 2, 5, 2)  # Intentar mover un alfil en línea recta, lo cual es inválido
        self.assertIsNotNone(chess_game.__board__.get_piece(7, 2))  # Verificar que el alfil sigue en su posición inicial

    def test_pawn_movement(self):
        chess_game = Chess()
        chess_game.move(6, 4, 4, 4)  # Mover peón blanco hacia adelante dos espacios
        self.assertIsNone(chess_game.__board__.get_piece(6, 4))  # Verificar que la posición inicial está vacía
        self.assertIsNotNone(chess_game.__board__.get_piece(4, 4))  # Verificar que el peón está en la nueva posición
        self.assertEqual(chess_game.__board__.get_piece(4, 4).color, "WHITE")  # Verificar que la pieza es blanca

    def test_invalid_pawn_movement(self):
        chess_game = Chess()
        with self.assertRaises(InvalidMove):
            chess_game.move(6, 4, 5, 3)  # Intentar mover un peón en diagonal sin captura
        self.assertIsNotNone(chess_game.__board__.get_piece(6, 4))  # Verificar que el peón sigue en su posición original

    def test_stalemate_detection(self):
        chess_game = Chess()
        # Crear una situación de tablas
        # Los movimientos aquí deben configurarse para reflejar una situación real de empate

        self.assertTrue(chess_game.is_stalemate("BLACK"))  # Verificar que el juego está en tablas para el rey negro
        self.assertIsNone(chess_game.winner)  # Verificar que no hay ganador

    def test_move_out_of_board(self):
        chess_game = Chess()
        with self.assertRaises(OutOfBoard):
            chess_game.move(-1, 0, 2, 0)  # Intentar mover fuera del tablero
        self.assertEqual(chess_game.turn, "WHITE")  # Verificar que el turno no cambió

if __name__ == "__main__":
    unittest.main()
