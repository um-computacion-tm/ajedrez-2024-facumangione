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
        
if __name__ == "__main__":
    unittest.main()