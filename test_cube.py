import unittest
from cube import Cube


class TestEvenCube(unittest.TestCase):
    def setUp(self):
        self.cube = Cube(2)

    def test_pieces_initialised_correctly_for_even_cube(self):
        pieces = self.cube.pieces
        self.assertEqual(len(pieces), 8)
        self.assertEqual(set(pieces.keys()), {
            (-1, -1, -1), (-1, -1, 1), (-1, 1, -1), (-1, 1, 1),
            (1, -1, -1), (1, -1, 1), (1, 1, -1), (1, 1, 1),
        })


class TestOddCube(unittest.TestCase):
    def setUp(self):
        self.cube = Cube(3)

    def test_pieces_initialised_correctly_for_odd_cube(self):
        pieces = self.cube.pieces
        self.assertEqual(set(pieces.keys()), {
            (-1, -1, -1), (-1, -1, 0), (-1, -1, 1), (-1, 0, -1), (-1, 0, 0), (-1, 0, 1), (-1, 1, -1), (-1, 1, 0), (-1, 1, 1),
            (0, -1, -1), (0, -1, 0), (0, -1, 1), (0, 0, -1), (0, 0, 0), (0, 0, 1), (0, 1, -1), (0, 1, 0), (0, 1, 1),
            (1, -1, -1), (1, -1, 0), (1, -1, 1), (1, 0, -1), (1, 0, 0), (1, 0, 1), (1, 1, -1), (1, 1, 0), (1, 1, 1),
        })

