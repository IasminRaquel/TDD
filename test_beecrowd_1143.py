from beecrowd_1143 import quadrado
import unittest

class Test_quadrado(unittest.TestCase):

    def test_multiplos(self):
        self.assertEqual(quadrado(5), ['1 1 1', '2 4 8', '3 9 27', '4 16 64', '5 25 125'])
        self.assertEqual(quadrado(1), ['1 1 1'])
        self.assertEqual(quadrado(7), ['1 1 1', '2 4 8', '3 9 27', '4 16 64', '5 25 125', '6 36 216', '7 49 343'])

if __name__ == '__main__':
    unittest.main()