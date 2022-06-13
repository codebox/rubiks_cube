import unittest

from cube import Cube, Direction, Rotation

LUF = (-1, 1, 1)
RUF = (1, 1, 1)
LDF = (-1, -1, 1)
RDF = (1, -1, 1)
LUB = (-1, 1, -1)
RUB = (1, 1, -1)
LDB = (-1, -1, -1)
RDB = (1, -1, -1)

class TestEvenCube(unittest.TestCase):

    def setUp(self):
        self.cube = Cube(2)

    def assert_piece_state(self, initial_coords, expected_coords, expected_rotation):
        piece = next(p for p in self.cube.pieces if p.initial_coords == initial_coords)
        self.assertEqual(piece.coords, expected_coords,
                         "Expected piece with initial_coord {} to be at {} but instead it was at {}".
                         format(initial_coords, expected_coords, piece.coords))
        self.assertEqual(piece.rotation, expected_rotation,
                         "Expected piece with initial_coord {} to have rotation {} but instead it was {}".
                         format(initial_coords, expected_rotation, piece.rotation))

    def assert_pieces_not_affected(self, *initial_coords):
        for ic in initial_coords:
            self.assert_piece_state(ic, ic, Rotation(0, 0, 0))

    def test_pieces_initialised_correctly_for_even_cube(self):
        pieces = self.cube.pieces
        self.assertEqual(len(pieces), 8)
        self.assertEqual(set([p.coords for p in pieces]), {LUF, RUF, LDF, RDF, LUB, RUB, LDB, RDB})

    def test_f1_move_applied_correctly(self):
        self.cube.move(Direction.FRONT, 1)
        # Back face
        self.assert_pieces_not_affected(LDB, RDB, LUB, RUB)
        # Front face
        self.assert_piece_state(LDF, LUF, Rotation(0, 0, 1))
        self.assert_piece_state(RDF, LDF, Rotation(0, 0, 1))
        self.assert_piece_state(LUF, RUF, Rotation(0, 0, 1))
        self.assert_piece_state(RUF, RDF, Rotation(0, 0, 1))

    def test_f2_move_applied_correctly(self):
        self.cube.move(Direction.FRONT, 2)
        # Back face
        self.assert_pieces_not_affected(LDB, RDB, LUB, RUB)
        # Front face
        self.assert_piece_state(LDF, RUF, Rotation(0, 0, 2))
        self.assert_piece_state(RDF, LUF, Rotation(0, 0, 2))
        self.assert_piece_state(LUF, RDF, Rotation(0, 0, 2))
        self.assert_piece_state(RUF, LDF, Rotation(0, 0, 2))

    def test_f_minus_1_move_applied_correctly(self):
        self.cube.move(Direction.FRONT, -1)
        # Back face
        self.assert_pieces_not_affected(LDB, RDB, LUB, RUB)
        # Front face
        self.assert_piece_state(LDF, RDF, Rotation(0, 0, 3))
        self.assert_piece_state(RDF, RUF, Rotation(0, 0, 3))
        self.assert_piece_state(LUF, LDF, Rotation(0, 0, 3))
        self.assert_piece_state(RUF, LUF, Rotation(0, 0, 3))

    def test_u1_move_applied_correctly(self):
        self.cube.move(Direction.UP, 1)
        # Down face
        self.assert_pieces_not_affected(LDB, LDF, RDB, RDF)
        # Up face
        self.assert_piece_state(LUB, RUB, Rotation(0, 1, 0))
        self.assert_piece_state(RUB, RUF, Rotation(0, 1, 0))
        self.assert_piece_state(RUF, LUF, Rotation(0, 1, 0))
        self.assert_piece_state(LUF, LUB, Rotation(0, 1, 0))

    def test_u2_move_applied_correctly(self):
        self.cube.move(Direction.UP, 2)
        # Down face
        self.assert_pieces_not_affected(LDB, LDF, RDB, RDF)
        # Up face
        self.assert_piece_state(LUB, RUF, Rotation(0, 2, 0))
        self.assert_piece_state(RUB, LUF, Rotation(0, 2, 0))
        self.assert_piece_state(RUF, LUB, Rotation(0, 2, 0))
        self.assert_piece_state(LUF, RUB, Rotation(0, 2, 0))

    def test_u_minus_1_move_applied_correctly(self):
        self.cube.move(Direction.UP, -1)
        # Down face
        self.assert_pieces_not_affected(LDB, LDF, RDB, RDF)
        # Up face
        self.assert_piece_state(LUB, LUF, Rotation(0, 3, 0))
        self.assert_piece_state(RUB, LUB, Rotation(0, 3, 0))
        self.assert_piece_state(RUF, RUB, Rotation(0, 3, 0))
        self.assert_piece_state(LUF, RUF, Rotation(0, 3, 0))

    def test_r1_move_applied_correctly(self):
        self.cube.move(Direction.RIGHT, 1)
        # Left face
        self.assert_pieces_not_affected(LDB, LUB, LDF, LUF)
        # Right face
        self.assert_piece_state(RUB, RDB, Rotation(1, 0, 0))
        self.assert_piece_state(RDB, RDF, Rotation(1, 0, 0))
        self.assert_piece_state(RUF, RUB, Rotation(1, 0, 0))
        self.assert_piece_state(RDF, RUF, Rotation(1, 0, 0))

    def test_r2_move_applied_correctly(self):
        self.cube.move(Direction.RIGHT, 2)
        # Left face
        self.assert_pieces_not_affected(LDB, LUB, LDF, LUF)
        # Right face
        self.assert_piece_state(RUB, RDF, Rotation(2, 0, 0))
        self.assert_piece_state(RDB, RUF, Rotation(2, 0, 0))
        self.assert_piece_state(RUF, RDB, Rotation(2, 0, 0))
        self.assert_piece_state(RDF, RUB, Rotation(2, 0, 0))

    def test_r_minus_1_move_applied_correctly(self):
        self.cube.move(Direction.RIGHT, -1)
        # Left face
        self.assert_pieces_not_affected(LDB, LUB, LDF, LUF)
        # Right face
        self.assert_piece_state(RUB, RUF, Rotation(3, 0, 0))
        self.assert_piece_state(RUF, RDF, Rotation(3, 0, 0))
        self.assert_piece_state(RDF, RDB, Rotation(3, 0, 0))
        self.assert_piece_state(RDB, RUB, Rotation(3, 0, 0))

    def test_b1_move_applied_correctly(self):
        pass

    def test_b2_move_applied_correctly(self):
        pass

    def test_b_minus_1_move_applied_correctly(self):
        pass

    def test_d1_move_applied_correctly(self):
        pass

    def test_d2_move_applied_correctly(self):
        pass

    def test_d_minus_1_move_applied_correctly(self):
        pass

    def test_l1_move_applied_correctly(self):
        pass

    def test_l2_move_applied_correctly(self):
        pass

    def test_l_minus_1_move_applied_correctly(self):
        pass

class TestOddCube(unittest.TestCase):
    def setUp(self):
        self.cube = Cube(3)

    def test_pieces_initialised_correctly_for_odd_cube(self):
        pieces = self.cube.pieces
        self.assertEqual(set([p.coords for p in pieces]), {
            (-1, -1, -1), (-1, -1, 0), (-1, -1, 1), (-1, 0, -1), (-1, 0, 0), (-1, 0, 1), (-1, 1, -1), (-1, 1, 0),
            (-1, 1, 1),
            (0, -1, -1), (0, -1, 0), (0, -1, 1), (0, 0, -1), (0, 0, 0), (0, 0, 1), (0, 1, -1), (0, 1, 0), (0, 1, 1),
            (1, -1, -1), (1, -1, 0), (1, -1, 1), (1, 0, -1), (1, 0, 0), (1, 0, 1), (1, 1, -1), (1, 1, 0), (1, 1, 1),
        })
