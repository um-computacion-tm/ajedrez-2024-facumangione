import unittest
from game.pieces.king import King

class TestRey(unittest.TestCase):
#Verifica que el método __str__ de la clase Rey retorne 'K' para un rey blanco y 'k' para un rey negro.
    def test_representacion_str(self):
        rey_blanco = King('WHITE')
        rey_negro = King('BLACK')
        self.assertEqual(rey_blanco.__str__(), 'K')
        self.assertEqual(rey_negro.__str__(), 'k')

#Evalúa que el rey blanco en el centro del tablero tenga los movimientos esperados usando el método possible_moves.

    def test_movimientos_rey_blanco(self):
        rey = King('WHITE')
        fila, columna = 4, 4
        movimientos_esperados = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
        movimientos = rey.possible_moves(fila, columna)
        self.assertCountEqual(movimientos, movimientos_esperados)

#Comprueba que el rey negro, situado en la misma posición central, pueda realizar los movimientos correctos.

    def test_movimientos_rey_negro(self):
        rey = King('BLACK')
        fila, columna = 4, 4
        movimientos_esperados = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
        movimientos = rey.possible_moves(fila, columna)
        self.assertCountEqual(movimientos, movimientos_esperados)

if __name__ == '__main__':
    unittest.main()
