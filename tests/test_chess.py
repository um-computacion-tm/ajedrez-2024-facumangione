import unittest
from game.chess import Chess
from game.exceptions import NonPieceOriginError, WrongTurnError, InvalidPieceMoveError

class TestAjedrez(unittest.TestCase):
#Esta función verifica que un objeto Chess se inicializa correctamente, asegurando que el turno inicial es de las piezas blancas y que el tablero esté bien configurado.
    def test_inicializacion(self):
        partida = Chess()  
        self.assertEqual(partida.turn, "WHITE")
        tablero = partida.get_board()
        self.assertIsNotNone(tablero)

#Esta función verifica que un peón blanco se mueva correctamente. Se asegura de que la posición final del peón no esté vacía, lo que indica que se movió correctamente.
    def test_mover_peon_valido(self):
        partida = Chess()
        partida.move(6, 0, 4, 0)
        self.assertEqual(partida.turn, "BLACK")
        self.assertEqual(partida.get_board()[6][0], '.')
        self.assertIsNotNone(partida.get_board()[4][0])

#Esta función verifica que un caballo se mueva correctamente en el tablero. Confirma que la nueva posición del caballo no está vacía.
    def test_mover_caballo_valido(self):
        partida = Chess()
        partida.move(7, 1, 5, 2)
        self.assertEqual(partida.turn, "BLACK")
        self.assertEqual(partida.get_board()[7][1], '.')
        self.assertIsNotNone(partida.get_board()[5][2])

#Verifica el comportamiento del método move cuando no hay una pieza en la posición de origen, y asegura que se lance la excepción NonPieceOriginError
    def test_mover_sin_pieza1(self):
        partida = Chess()
        with self.assertRaises(NonPieceOriginError) as contexto:
            partida.move(3, 3, 4, 3)
        self.assertEqual(str(contexto.exception), "There is no piece at the origin position.")

#Verifica el comportamiento del método move cuando no hay una pieza en otra posición de origen, y asegura que se lance la excepción NonPieceOriginError.
    def test_mover_sin_pieza2(self):
        partida = Chess()
        with self.assertRaises(NonPieceOriginError) as contexto:
            partida.move(3, 4, 4, 4)
        self.assertEqual(str(contexto.exception), "There is no piece at the origin position.")

#Verifica que cuando se intenta mover una pieza que no pertenece al jugador que tiene el turno, se lanza la excepción WrongTurnError.
    def test_turno_incorrecto(self):
        partida = Chess()
        partida.move(6, 0, 4, 0)
        with self.assertRaises(WrongTurnError) as contexto:
            partida.move(6, 1, 5, 2)
        self.assertEqual(str(contexto.exception), "It is not the turn of the selected piece.")

#Verifica que cuando se intenta mover una pieza a una posición inválida, se lanza la excepción InvalidPieceMoveError.
    def test_movimiento_invalido(self):
        partida = Chess()
        with self.assertRaises(InvalidPieceMoveError) as contexto:
            partida.move(6, 0, 3, 0)
        self.assertEqual(str(contexto.exception), "Invalid move for the selected piece.")

#Verifica que el método para cambiar de turno funcione correctamente después de cada movimiento válido.
    def test_alternar_turno(self):
        partida = Chess()
        partida.move(6, 0, 4, 0)
        self.assertEqual(partida.turn, "BLACK")
        partida.move(1, 0, 3, 0)
        self.assertEqual(partida.turn, "WHITE")

if __name__ == '__main__':
    unittest.main()
