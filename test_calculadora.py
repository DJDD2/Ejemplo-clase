
import unittest
from calculadora import sumar, restar, dividir

class PruebasCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_resta(self):
        self.assertEqual(restar(8, 3), 5)

    def test_division(self):
        self.assertEqual(dividir(10, 2), 5.0)

if __name__ == "__main__":
    unittest.main()
