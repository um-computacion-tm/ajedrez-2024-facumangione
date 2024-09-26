import unittest
from game.pieces.knight import Knight

class TestCaballero(unittest.TestCase):

#La función test_convertir_a_str verifica que el método __str__ de la clase Knight retorne 'N' para una pieza blanca y 'n' para una pieza negra
    def test_convertir_a_str(self):
        caballero_blanco = Knight('WHITE')
        caballero_negro = Knight('BLACK')
        self.assertEqual(str(caballero_blanco), 'N')
        self.assertEqual(str(caballero_negro), 'n')

#La función test_generar_direcciones_caballero verifica que el método generate_knight_directions de la clase Knight retorne la lista correcta de direcciones de movimiento del caballero.
    def test_generar_direcciones_caballero(self):
        caballero = Knight('WHITE')
        direcciones_correctas = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        self.assertEqual(caballero.generate_knight_directions(), direcciones_correctas)

if __name__ == '__main__':
    unittest.main()
