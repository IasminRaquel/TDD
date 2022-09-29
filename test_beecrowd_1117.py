from beecrowd_1117 import notas_validas
import unittest

class Test_notas(unittest.TestCase):

    def test_notas_validas(self):
        self.assertEqual(notas_validas(8, 8), 8.0)
        self.assertEqual(notas_validas(6, 5), 5.5)
        self.assertEqual(notas_validas(3.5, 10), 6.75)
        self.assertEqual(notas_validas(0.1, 10), 5.05)
        self.assertEqual(notas_validas(8, -4), "alguma nota invalida")

if __name__ == '__main__':
    unittest.main()
