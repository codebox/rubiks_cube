import unittest

from cube import Orientation, Rotation, Direction, Face

class TestOrientation(unittest.TestCase):
    def setUp(self):
        self.orientation = Orientation()

    def assert_face_for_direction(self, direction, expected_face):
        self.assertEqual(self.orientation.get_face_for_direction(direction), expected_face)

    def test_f1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.FRONT, 1))

        self.assert_face_for_direction(Direction.UP, Face.LEFT)
        self.assert_face_for_direction(Direction.RIGHT, Face.UP)
        self.assert_face_for_direction(Direction.DOWN, Face.RIGHT)
        self.assert_face_for_direction(Direction.LEFT, Face.DOWN)
        self.assert_face_for_direction(Direction.FRONT, Face.FRONT)
        self.assert_face_for_direction(Direction.BACK, Face.BACK)

    def test_f2_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.FRONT, 2))

        self.assert_face_for_direction(Direction.UP, Face.DOWN)
        self.assert_face_for_direction(Direction.RIGHT, Face.LEFT)
        self.assert_face_for_direction(Direction.DOWN, Face.UP)
        self.assert_face_for_direction(Direction.LEFT, Face.RIGHT)
        self.assert_face_for_direction(Direction.FRONT, Face.FRONT)
        self.assert_face_for_direction(Direction.BACK, Face.BACK)

    def test_f_minus_1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.FRONT, -1))

        self.assert_face_for_direction(Direction.UP, Face.RIGHT)
        self.assert_face_for_direction(Direction.RIGHT, Face.DOWN)
        self.assert_face_for_direction(Direction.DOWN, Face.LEFT)
        self.assert_face_for_direction(Direction.LEFT, Face.UP)
        self.assert_face_for_direction(Direction.FRONT, Face.FRONT)
        self.assert_face_for_direction(Direction.BACK, Face.BACK)


    def test_u1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.UP, 1))

        self.assert_face_for_direction(Direction.UP, Face.UP)
        self.assert_face_for_direction(Direction.RIGHT, Face.BACK)
        self.assert_face_for_direction(Direction.DOWN, Face.DOWN)
        self.assert_face_for_direction(Direction.LEFT, Face.FRONT)
        self.assert_face_for_direction(Direction.FRONT, Face.RIGHT)
        self.assert_face_for_direction(Direction.BACK, Face.LEFT)

    def test_u2_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.UP, 2))

        self.assert_face_for_direction(Direction.UP, Face.UP)
        self.assert_face_for_direction(Direction.RIGHT, Face.LEFT)
        self.assert_face_for_direction(Direction.DOWN, Face.DOWN)
        self.assert_face_for_direction(Direction.LEFT, Face.RIGHT)
        self.assert_face_for_direction(Direction.FRONT, Face.BACK)
        self.assert_face_for_direction(Direction.BACK, Face.FRONT)

    def test_u_minus_1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.UP, -1))

        self.assert_face_for_direction(Direction.UP, Face.UP)
        self.assert_face_for_direction(Direction.RIGHT, Face.FRONT)
        self.assert_face_for_direction(Direction.DOWN, Face.DOWN)
        self.assert_face_for_direction(Direction.LEFT, Face.BACK)
        self.assert_face_for_direction(Direction.FRONT, Face.LEFT)
        self.assert_face_for_direction(Direction.BACK, Face.RIGHT)

    def test_r1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.RIGHT, 1))

        self.assert_face_for_direction(Direction.UP, Face.FRONT)
        self.assert_face_for_direction(Direction.RIGHT, Face.RIGHT)
        self.assert_face_for_direction(Direction.DOWN, Face.BACK)
        self.assert_face_for_direction(Direction.LEFT, Face.LEFT)
        self.assert_face_for_direction(Direction.FRONT, Face.DOWN)
        self.assert_face_for_direction(Direction.BACK, Face.UP)

    def test_r2_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.RIGHT, 2))

        self.assert_face_for_direction(Direction.UP, Face.DOWN)
        self.assert_face_for_direction(Direction.RIGHT, Face.RIGHT)
        self.assert_face_for_direction(Direction.DOWN, Face.UP)
        self.assert_face_for_direction(Direction.LEFT, Face.LEFT)
        self.assert_face_for_direction(Direction.FRONT, Face.BACK)
        self.assert_face_for_direction(Direction.BACK, Face.FRONT)

    def test_r_minus_1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.RIGHT, -1))

        self.assert_face_for_direction(Direction.UP, Face.BACK)
        self.assert_face_for_direction(Direction.RIGHT, Face.RIGHT)
        self.assert_face_for_direction(Direction.DOWN, Face.FRONT)
        self.assert_face_for_direction(Direction.LEFT, Face.LEFT)
        self.assert_face_for_direction(Direction.FRONT, Face.UP)
        self.assert_face_for_direction(Direction.BACK, Face.DOWN)

    def test_b1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.BACK, 1))

        self.assert_face_for_direction(Direction.UP, Face.RIGHT)
        self.assert_face_for_direction(Direction.RIGHT, Face.DOWN)
        self.assert_face_for_direction(Direction.DOWN, Face.LEFT)
        self.assert_face_for_direction(Direction.LEFT, Face.UP)
        self.assert_face_for_direction(Direction.FRONT, Face.FRONT)
        self.assert_face_for_direction(Direction.BACK, Face.BACK)

    def test_b2_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.BACK, 2))

        self.assert_face_for_direction(Direction.UP, Face.DOWN)
        self.assert_face_for_direction(Direction.RIGHT, Face.LEFT)
        self.assert_face_for_direction(Direction.DOWN, Face.UP)
        self.assert_face_for_direction(Direction.LEFT, Face.RIGHT)
        self.assert_face_for_direction(Direction.FRONT, Face.FRONT)
        self.assert_face_for_direction(Direction.BACK, Face.BACK)

    def test_b_minus_1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.BACK, -1))

        self.assert_face_for_direction(Direction.UP, Face.LEFT)
        self.assert_face_for_direction(Direction.RIGHT, Face.UP)
        self.assert_face_for_direction(Direction.DOWN, Face.RIGHT)
        self.assert_face_for_direction(Direction.LEFT, Face.DOWN)
        self.assert_face_for_direction(Direction.FRONT, Face.FRONT)
        self.assert_face_for_direction(Direction.BACK, Face.BACK)

    def test_d1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.DOWN, 1))

        self.assert_face_for_direction(Direction.UP, Face.UP)
        self.assert_face_for_direction(Direction.RIGHT, Face.FRONT)
        self.assert_face_for_direction(Direction.DOWN, Face.DOWN)
        self.assert_face_for_direction(Direction.LEFT, Face.BACK)
        self.assert_face_for_direction(Direction.FRONT, Face.LEFT)
        self.assert_face_for_direction(Direction.BACK, Face.RIGHT)

    def test_d2_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.DOWN, 2))

        self.assert_face_for_direction(Direction.UP, Face.UP)
        self.assert_face_for_direction(Direction.RIGHT, Face.LEFT)
        self.assert_face_for_direction(Direction.DOWN, Face.DOWN)
        self.assert_face_for_direction(Direction.LEFT, Face.RIGHT)
        self.assert_face_for_direction(Direction.FRONT, Face.BACK)
        self.assert_face_for_direction(Direction.BACK, Face.FRONT)


    def test_d_minus_1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.DOWN, -1))

        self.assert_face_for_direction(Direction.UP, Face.UP)
        self.assert_face_for_direction(Direction.RIGHT, Face.BACK)
        self.assert_face_for_direction(Direction.DOWN, Face.DOWN)
        self.assert_face_for_direction(Direction.LEFT, Face.FRONT)
        self.assert_face_for_direction(Direction.FRONT, Face.RIGHT)
        self.assert_face_for_direction(Direction.BACK, Face.LEFT)

    def test_l1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.LEFT, 1))

        self.assert_face_for_direction(Direction.UP, Face.BACK)
        self.assert_face_for_direction(Direction.RIGHT, Face.RIGHT)
        self.assert_face_for_direction(Direction.DOWN, Face.FRONT)
        self.assert_face_for_direction(Direction.LEFT, Face.LEFT)
        self.assert_face_for_direction(Direction.FRONT, Face.UP)
        self.assert_face_for_direction(Direction.BACK, Face.DOWN)

    def test_l2_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.LEFT, 2))

        self.assert_face_for_direction(Direction.UP, Face.DOWN)
        self.assert_face_for_direction(Direction.RIGHT, Face.RIGHT)
        self.assert_face_for_direction(Direction.DOWN, Face.UP)
        self.assert_face_for_direction(Direction.LEFT, Face.LEFT)
        self.assert_face_for_direction(Direction.FRONT, Face.BACK)
        self.assert_face_for_direction(Direction.BACK, Face.FRONT)

    def test_l_minus_1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.LEFT, -1))

        self.assert_face_for_direction(Direction.UP, Face.FRONT)
        self.assert_face_for_direction(Direction.RIGHT, Face.RIGHT)
        self.assert_face_for_direction(Direction.DOWN, Face.BACK)
        self.assert_face_for_direction(Direction.LEFT, Face.LEFT)
        self.assert_face_for_direction(Direction.FRONT, Face.DOWN)
        self.assert_face_for_direction(Direction.BACK, Face.UP)

    def test_ru_moves_applied_correctly(self):
        self.orientation.change(Rotation(Direction.RIGHT, 1))
        self.orientation.change(Rotation(Direction.UP, 1))

        self.assert_face_for_direction(Direction.UP, Face.FRONT)
        self.assert_face_for_direction(Direction.RIGHT, Face.UP)
        self.assert_face_for_direction(Direction.DOWN, Face.BACK)
        self.assert_face_for_direction(Direction.LEFT, Face.DOWN)
        self.assert_face_for_direction(Direction.FRONT, Face.RIGHT)
        self.assert_face_for_direction(Direction.BACK, Face.LEFT)

