import unittest

from cube import Cube


LUF = (-1, 1, 1)
RUF = (1, 1, 1)
LDF = (-1, -1, 1)
RDF = (1, -1, 1)
LUB = (-1, 1, -1)
RUB = (1, 1, -1)
LDB = (-1, -1, -1)
RDB = (1, -1, -1)
FU = (0, 1, 1)
FL = (-1, 0, 1)
FR = (1, 0, 1)
FD = (0, -1, 1)
BU = (0, 1, -1)
BL = (-1, 0, -1)
BR = (1, 0, -1)
BD = (0, -1, -1)
LU = (-1, 1, 0)
LD = (-1, -1, 0)
RU = (1, 1, 0)
RD = (1, -1, 0)
FC = (0,0,1)
BC = (0,0,-1)
LC = (-1,0,0)
RC = (1,0,0)
UC = (0,1,0)
DC = (0,-1,0)

class TestCube(unittest.TestCase):
    def assert_piece_position(self, initial_coords, expected_coords):
        piece = next(p for p in self.cube.pieces if p.initial_coords == initial_coords)
        self.assertEqual(piece.coords, expected_coords,
                         "Expected piece with initial_coord {} to be at {} but instead it was at {}".
                         format(initial_coords, expected_coords, piece.coords))

    def assert_pieces_not_affected(self, *initial_coords):
        for ic in initial_coords:
            self.assert_piece_position(ic, ic)


class TestEvenCube(TestCube):
    def setUp(self):
        self.cube = Cube(2)

    def test_pieces_initialised_correctly_for_even_cube(self):
        pieces = self.cube.pieces
        self.assertEqual(len(pieces), 8)
        self.assertEqual(set([p.coords for p in pieces]), {LUF, RUF, LDF, RDF, LUB, RUB, LDB, RDB})

    def test_f1_move_applied_correctly(self):
        self.cube.sequence('F')
        # Back face
        self.assert_pieces_not_affected(LDB, RDB, LUB, RUB)
        # Front face
        self.assert_piece_position(LDF, LUF)
        self.assert_piece_position(RDF, LDF)
        self.assert_piece_position(LUF, RUF)
        self.assert_piece_position(RUF, RDF)

    def test_f2_move_applied_correctly(self):
        self.cube.sequence('F2')
        # Back face
        self.assert_pieces_not_affected(LDB, RDB, LUB, RUB)
        # Front face
        self.assert_piece_position(LDF, RUF)
        self.assert_piece_position(RDF, LUF)
        self.assert_piece_position(LUF, RDF)
        self.assert_piece_position(RUF, LDF)

    def test_f_minus_1_move_applied_correctly(self):
        self.cube.sequence('F-')
        # Back face
        self.assert_pieces_not_affected(LDB, RDB, LUB, RUB)
        # Front face
        self.assert_piece_position(LDF, RDF)
        self.assert_piece_position(RDF, RUF)
        self.assert_piece_position(LUF, LDF)
        self.assert_piece_position(RUF, LUF)

    def test_u1_move_applied_correctly(self):
        self.cube.sequence('U')
        # Down face
        self.assert_pieces_not_affected(LDB, LDF, RDB, RDF)
        # Up face
        self.assert_piece_position(LUB, RUB)
        self.assert_piece_position(RUB, RUF)
        self.assert_piece_position(RUF, LUF)
        self.assert_piece_position(LUF, LUB)

    def test_u2_move_applied_correctly(self):
        self.cube.sequence('U2')
        # Down face
        self.assert_pieces_not_affected(LDB, LDF, RDB, RDF)
        # Up face
        self.assert_piece_position(LUB, RUF)
        self.assert_piece_position(RUB, LUF)
        self.assert_piece_position(RUF, LUB)
        self.assert_piece_position(LUF, RUB)

    def test_u_minus_1_move_applied_correctly(self):
        self.cube.sequence('U-')
        # Down face
        self.assert_pieces_not_affected(LDB, LDF, RDB, RDF)
        # Up face
        self.assert_piece_position(LUB, LUF)
        self.assert_piece_position(RUB, LUB)
        self.assert_piece_position(RUF, RUB)
        self.assert_piece_position(LUF, RUF)

    def test_r1_move_applied_correctly(self):
        self.cube.sequence('R')
        # Left face
        self.assert_pieces_not_affected(LDB, LUB, LDF, LUF)
        # Right face
        self.assert_piece_position(RUB, RDB)
        self.assert_piece_position(RDB, RDF)
        self.assert_piece_position(RUF, RUB)
        self.assert_piece_position(RDF, RUF)

    def test_r2_move_applied_correctly(self):
        self.cube.sequence('R2')
        # Left face
        self.assert_pieces_not_affected(LDB, LUB, LDF, LUF)
        # Right face
        self.assert_piece_position(RUB, RDF)
        self.assert_piece_position(RDB, RUF)
        self.assert_piece_position(RUF, RDB)
        self.assert_piece_position(RDF, RUB)

    def test_r_minus_1_move_applied_correctly(self):
        self.cube.sequence('R-')
        # Left face
        self.assert_pieces_not_affected(LDB, LUB, LDF, LUF)
        # Right face
        self.assert_piece_position(RUB, RUF)
        self.assert_piece_position(RUF, RDF)
        self.assert_piece_position(RDF, RDB)
        self.assert_piece_position(RDB, RUB)

    def test_b1_move_applied_correctly(self):
        self.cube.sequence('B')
        # Front face
        self.assert_pieces_not_affected(LUF, RUF, LDF, RDF)
        # Back face
        self.assert_piece_position(LUB, LDB)
        self.assert_piece_position(RUB, LUB)
        self.assert_piece_position(LDB, RDB)
        self.assert_piece_position(RDB, RUB)

    def test_b2_move_applied_correctly(self):
        self.cube.sequence('B2')
        # Front face
        self.assert_pieces_not_affected(LUF, RUF, LDF, RDF)
        # Back face
        self.assert_piece_position(LUB, RDB)
        self.assert_piece_position(RUB, LDB)
        self.assert_piece_position(LDB, RUB)
        self.assert_piece_position(RDB, LUB)

    def test_b_minus_1_move_applied_correctly(self):
        self.cube.sequence('B-')
        # Front face
        self.assert_pieces_not_affected(LUF, RUF, LDF, RDF)
        # Back face
        self.assert_piece_position(LUB, RUB)
        self.assert_piece_position(RUB, RDB)
        self.assert_piece_position(LDB, LUB)
        self.assert_piece_position(RDB, LDB)

    def test_d1_move_applied_correctly(self):
        self.cube.sequence('D')
        # Up face
        self.assert_pieces_not_affected(LUF, RUF, LUB, RUB)
        # Down face
        self.assert_piece_position(LDB, LDF)
        self.assert_piece_position(RDB, LDB)
        self.assert_piece_position(LDF, RDF)
        self.assert_piece_position(RDF, RDB)

    def test_d2_move_applied_correctly(self):
        self.cube.sequence('D2')
        # Up face
        self.assert_pieces_not_affected(LUF, RUF, LUB, RUB)
        # Down face
        self.assert_piece_position(LDB, RDF)
        self.assert_piece_position(RDB, LDF)
        self.assert_piece_position(LDF, RDB)
        self.assert_piece_position(RDF, LDB)

    def test_d_minus_1_move_applied_correctly(self):
        self.cube.sequence('D-')
        # Up face
        self.assert_pieces_not_affected(LUF, RUF, LUB, RUB)
        # Down face
        self.assert_piece_position(LDB, RDB)
        self.assert_piece_position(RDB, RDF)
        self.assert_piece_position(LDF, LDB)
        self.assert_piece_position(RDF, LDF)

    def test_l1_move_applied_correctly(self):
        self.cube.sequence('L')
        # Right face
        self.assert_pieces_not_affected(RUF, RUB, RDB, RDF)
        # Left face
        self.assert_piece_position(LUF, LDF)
        self.assert_piece_position(LUB, LUF)
        self.assert_piece_position(LDF, LDB)
        self.assert_piece_position(LDB, LUB)

    def test_l2_move_applied_correctly(self):
        self.cube.sequence('L2')
        # Right face
        self.assert_pieces_not_affected(RUF, RUB, RDB, RDF)
        # Left face
        self.assert_piece_position(LUF, LDB)
        self.assert_piece_position(LUB, LDF)
        self.assert_piece_position(LDF, LUB)
        self.assert_piece_position(LDB, LUF)

    def test_l_minus_1_move_applied_correctly(self):
        self.cube.sequence('L-')
        # Right face
        self.assert_pieces_not_affected(RUF, RUB, RDB, RDF)
        # Left face
        self.assert_piece_position(LUF, LUB)
        self.assert_piece_position(LUB, LDB)
        self.assert_piece_position(LDF, LUF)
        self.assert_piece_position(LDB, LDF)


class TestOddCube(TestCube):
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

    def test_m_move_applied_correctly(self):
        self.cube.sequence('M')
        # Right face
        self.assert_pieces_not_affected(RUF, RUB, RDB, RDF, FR, BR, RU, RD)
        # Left face
        self.assert_pieces_not_affected(LUF, LUB, LDB, LDF, FL, BL, LU, LD)

        # Middle slice face
        self.assert_piece_position(FC, DC)
        self.assert_piece_position(DC, BC)
        self.assert_piece_position(BC, UC)
        self.assert_piece_position(UC, FC)

        self.assert_piece_position(FU, FD)
        self.assert_piece_position(FD, BD)
        self.assert_piece_position(BD, BU)
        self.assert_piece_position(BU, FU)

    def test_m2_move_applied_correctly(self):
        self.cube.sequence('M2')
        # Right face
        self.assert_pieces_not_affected(RUF, RUB, RDB, RDF, FR, BR, RU, RD)
        # Left face
        self.assert_pieces_not_affected(LUF, LUB, LDB, LDF, FL, BL, LU, LD)

        # Middle slice face
        self.assert_piece_position(FC, BC)
        self.assert_piece_position(DC, UC)
        self.assert_piece_position(BC, FC)
        self.assert_piece_position(UC, DC)

        self.assert_piece_position(FU, BD)
        self.assert_piece_position(FD, BU)
        self.assert_piece_position(BD, FU)
        self.assert_piece_position(BU, FD)

    def test_m_minus_1_move_applied_correctly(self):
        self.cube.sequence('M-')
        # Right face
        self.assert_pieces_not_affected(RUF, RUB, RDB, RDF, FR, BR, RU, RD)
        # Left face
        self.assert_pieces_not_affected(LUF, LUB, LDB, LDF, FL, BL, LU, LD)

        # Middle slice face
        self.assert_piece_position(FC, UC)
        self.assert_piece_position(UC, BC)
        self.assert_piece_position(BC, DC)
        self.assert_piece_position(DC, FC)

        self.assert_piece_position(FU, BU)
        self.assert_piece_position(FD, FU)
        self.assert_piece_position(BD, FD)
        self.assert_piece_position(BU, BD)

    def test_e_move_applied_correctly(self):
        self.cube.sequence('E')
        # Top face
        self.assert_pieces_not_affected(RUF, RUB, LUF, LUB, FU, LU, BU, RU)
        # Down face
        self.assert_pieces_not_affected(RDF, RDB, LDF, LDB, FD, LD, BD, RD)

        # Middle slice face
        self.assert_piece_position(FC, RC)
        self.assert_piece_position(RC, BC)
        self.assert_piece_position(BC, LC)
        self.assert_piece_position(LC, FC)

        self.assert_piece_position(FL, FR)
        self.assert_piece_position(FR, BR)
        self.assert_piece_position(BR, BL)
        self.assert_piece_position(BL, FL)

    def test_e2_move_applied_correctly(self):
        self.cube.sequence('E2')
        # Top face
        self.assert_pieces_not_affected(RUF, RUB, LUF, LUB, FU, LU, BU, RU)
        # Down face
        self.assert_pieces_not_affected(RDF, RDB, LDF, LDB, FD, LD, BD, RD)

        # Middle slice face
        self.assert_piece_position(FC, BC)
        self.assert_piece_position(RC, LC)
        self.assert_piece_position(BC, FC)
        self.assert_piece_position(LC, RC)

        self.assert_piece_position(FL, BR)
        self.assert_piece_position(FR, BL)
        self.assert_piece_position(BR, FL)
        self.assert_piece_position(BL, FR)

    def test_e_minus_1_move_applied_correctly(self):
        self.cube.sequence('E-')
        # Top face
        self.assert_pieces_not_affected(RUF, RUB, LUF, LUB, FU, LU, BU, RU)
        # Down face
        self.assert_pieces_not_affected(RDF, RDB, LDF, LDB, FD, LD, BD, RD)

        # Middle slice face
        self.assert_piece_position(FC, LC)
        self.assert_piece_position(RC, FC)
        self.assert_piece_position(BC, RC)
        self.assert_piece_position(LC, BC)

        self.assert_piece_position(FL, BL)
        self.assert_piece_position(FR, FL)
        self.assert_piece_position(BR, FR)
        self.assert_piece_position(BL, BR)

    def test_s_move_applied_correctly(self):
        self.cube.sequence('S')
        # Front face
        self.assert_pieces_not_affected(RUF, LUF, RDF, LDF, FU, FL, FR, FD)
        # Back face
        self.assert_pieces_not_affected(RUB, LUB, RDB, LDB, BU, BL, BR, BD)

        # Middle slice face
        self.assert_piece_position(LC, UC)
        self.assert_piece_position(UC, RC)
        self.assert_piece_position(RC, DC)
        self.assert_piece_position(DC, LC)

        self.assert_piece_position(LU, RU)
        self.assert_piece_position(RU, RD)
        self.assert_piece_position(RD, LD)
        self.assert_piece_position(LD, LU)

    def test_s2_move_applied_correctly(self):
        self.cube.sequence('S2')
        # Front face
        self.assert_pieces_not_affected(RUF, LUF, RDF, LDF, FU, FL, FR, FD)
        # Back face
        self.assert_pieces_not_affected(RUB, LUB, RDB, LDB, BU, BL, BR, BD)

        # Middle slice face
        self.assert_piece_position(LC, RC)
        self.assert_piece_position(UC, DC)
        self.assert_piece_position(RC, LC)
        self.assert_piece_position(DC, UC)

        self.assert_piece_position(LU, RD)
        self.assert_piece_position(RU, LD)
        self.assert_piece_position(RD, LU)
        self.assert_piece_position(LD, RU)

    def test_s_minus_1_move_applied_correctly(self):
        self.cube.sequence('S-')
        # Front face
        self.assert_pieces_not_affected(RUF, LUF, RDF, LDF, FU, FL, FR, FD)
        # Back face
        self.assert_pieces_not_affected(RUB, LUB, RDB, LDB, BU, BL, BR, BD)

        # Middle slice face
        self.assert_piece_position(LC, DC)
        self.assert_piece_position(UC, LC)
        self.assert_piece_position(RC, UC)
        self.assert_piece_position(DC, RC)

        self.assert_piece_position(LU, LD)
        self.assert_piece_position(RU, LU)
        self.assert_piece_position(RD, RU)
        self.assert_piece_position(LD, RD)