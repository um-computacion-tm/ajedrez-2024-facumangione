import unittest
from game.board import Board
from game.chess import Chess
from game.exceptions import InvalidMove, InvalidMoveNoPiece, InvalidMoveRookMove, OutOfBoard

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
