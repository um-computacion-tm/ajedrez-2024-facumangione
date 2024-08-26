import unittest
from game.board import Board
from game.chess import Chess

class TestChess(unittest.TestCase):
    def setUp(self):
        #inicializa un nuevo tablero.
        self.board = Board()

    def test_initial_turn(self):
        chess_game = Chess () #nueva partida
        self.assertEqual(chess_game.turn, "WHITE") #verifico que el 1er turno sea del blanco

    def test_turn_change_correctly(self):
        chess_game = Chess () #nueva partida
        self.assertEqual(chess_game.turn, "WHITE") #verifico que el 1er turno sea del blanco

        #debo de realizar un movimiento como 2do paso
        chess_game.move (0,0,1,0) #aca supongo que el movimiento es valido (luego en el test_board verificare si lo es o no)
        "(fila origen, columna origen, fila destino, columna destino)"


        #verifico el cambio de turno (que es lo que busco)
        self.assertEqual(chess_game.turn, "BLACK")

    def test_turn_does_not_change_on_invalid_move(self):
        chess_game = Chess()
        chess_game.move(4, 4, 5, 5)  # Movimiento sin pieza en la posición de origen
        self.assertEqual(chess_game.turn, "WHITE")  # El turno no debería cambiar
        
    def test_piece_capture(self):
        chess_game = Chess()
        chess_game.move(6, 4, 4, 4)  # Mover peón blanco
        chess_game.move(1, 3, 3, 3)  # Mover peón negro
        chess_game.move(4, 4, 3, 3)  # Captura el peón negro

        self.assertIsNone(chess_game.board.get_piece(4, 4))  # Verificar que la posición original está vacía
        self.assertIsNotNone(chess_game.board.get_piece(3, 3))  # Verificar que el peón blanco ocupa la posición del peón negro
        self.assertEqual(chess_game.board.get_piece(3, 3).color, "WHITE")  # Verificar que la pieza capturada es blanca
        
    def test_invalid_piece_movement(self):
        chess_game = Chess()
        chess_game.move(0, 0, 3, 0)  # Intentar mover una torre desde (0, 0) a (3, 0), lo cual es inválido al inicio
        self.assertIsNotNone(chess_game.board.get_piece(0, 0))  # Verificar que la torre sigue en su lugar original
        self.assertIsNone(chess_game.board.get_piece(3, 0))  # Verificar que la posición destino está vacía
        self.assertEqual(chess_game.turn, "WHITE")  # Verificar que el turno no cambió
    

        
if __name__ == "__main__":
    unittest.main()