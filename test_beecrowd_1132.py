from beecrowd_1132 import multiplos
import unittest

class Test_multiplos(unittest.TestCase):

    def test_multiplos(self):
        self.assertEqual(multiplos(80, 100), 1799)
        self.assertEqual(multiplos(100, 200), 13954)
        self.assertEqual(multiplos(200, 87), 15072)
        self.assertEqual(multiplos(500, 550), 24669)

if __name__ == '__main__':
    unittest.main()