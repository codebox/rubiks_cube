import unittest

from direction import Direction
from orientation import Orientation
from rotation import Rotation


class TestOrientation(unittest.TestCase):
    def setUp(self):
        self.orientation = Orientation()

    def assert_face_for_direction(self, direction, expected_face):
        self.assertEqual(self.orientation.get_face_for_direction(direction), expected_face)

    def test_f1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.FRONT, 1))

        self.assert_face_for_direction(Direction.UP, Direction.LEFT)
        self.assert_face_for_direction(Direction.RIGHT, Direction.UP)
        self.assert_face_for_direction(Direction.DOWN, Direction.RIGHT)
        self.assert_face_for_direction(Direction.LEFT, Direction.DOWN)
        self.assert_face_for_direction(Direction.FRONT, Direction.FRONT)
        self.assert_face_for_direction(Direction.BACK, Direction.BACK)

    def test_f2_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.FRONT, 2))

        self.assert_face_for_direction(Direction.UP, Direction.DOWN)
        self.assert_face_for_direction(Direction.RIGHT, Direction.LEFT)
        self.assert_face_for_direction(Direction.DOWN, Direction.UP)
        self.assert_face_for_direction(Direction.LEFT, Direction.RIGHT)
        self.assert_face_for_direction(Direction.FRONT, Direction.FRONT)
        self.assert_face_for_direction(Direction.BACK, Direction.BACK)

    def test_f_minus_1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.FRONT, -1))

        self.assert_face_for_direction(Direction.UP, Direction.RIGHT)
        self.assert_face_for_direction(Direction.RIGHT, Direction.DOWN)
        self.assert_face_for_direction(Direction.DOWN, Direction.LEFT)
        self.assert_face_for_direction(Direction.LEFT, Direction.UP)
        self.assert_face_for_direction(Direction.FRONT, Direction.FRONT)
        self.assert_face_for_direction(Direction.BACK, Direction.BACK)


    def test_u1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.UP, 1))

        self.assert_face_for_direction(Direction.UP, Direction.UP)
        self.assert_face_for_direction(Direction.RIGHT, Direction.BACK)
        self.assert_face_for_direction(Direction.DOWN, Direction.DOWN)
        self.assert_face_for_direction(Direction.LEFT, Direction.FRONT)
        self.assert_face_for_direction(Direction.FRONT, Direction.RIGHT)
        self.assert_face_for_direction(Direction.BACK, Direction.LEFT)

    def test_u2_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.UP, 2))

        self.assert_face_for_direction(Direction.UP, Direction.UP)
        self.assert_face_for_direction(Direction.RIGHT, Direction.LEFT)
        self.assert_face_for_direction(Direction.DOWN, Direction.DOWN)
        self.assert_face_for_direction(Direction.LEFT, Direction.RIGHT)
        self.assert_face_for_direction(Direction.FRONT, Direction.BACK)
        self.assert_face_for_direction(Direction.BACK, Direction.FRONT)

    def test_u_minus_1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.UP, -1))

        self.assert_face_for_direction(Direction.UP, Direction.UP)
        self.assert_face_for_direction(Direction.RIGHT, Direction.FRONT)
        self.assert_face_for_direction(Direction.DOWN, Direction.DOWN)
        self.assert_face_for_direction(Direction.LEFT, Direction.BACK)
        self.assert_face_for_direction(Direction.FRONT, Direction.LEFT)
        self.assert_face_for_direction(Direction.BACK, Direction.RIGHT)

    def test_r1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.RIGHT, 1))

        self.assert_face_for_direction(Direction.UP, Direction.FRONT)
        self.assert_face_for_direction(Direction.RIGHT, Direction.RIGHT)
        self.assert_face_for_direction(Direction.DOWN, Direction.BACK)
        self.assert_face_for_direction(Direction.LEFT, Direction.LEFT)
        self.assert_face_for_direction(Direction.FRONT, Direction.DOWN)
        self.assert_face_for_direction(Direction.BACK, Direction.UP)

    def test_r2_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.RIGHT, 2))

        self.assert_face_for_direction(Direction.UP, Direction.DOWN)
        self.assert_face_for_direction(Direction.RIGHT, Direction.RIGHT)
        self.assert_face_for_direction(Direction.DOWN, Direction.UP)
        self.assert_face_for_direction(Direction.LEFT, Direction.LEFT)
        self.assert_face_for_direction(Direction.FRONT, Direction.BACK)
        self.assert_face_for_direction(Direction.BACK, Direction.FRONT)

    def test_r_minus_1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.RIGHT, -1))

        self.assert_face_for_direction(Direction.UP, Direction.BACK)
        self.assert_face_for_direction(Direction.RIGHT, Direction.RIGHT)
        self.assert_face_for_direction(Direction.DOWN, Direction.FRONT)
        self.assert_face_for_direction(Direction.LEFT, Direction.LEFT)
        self.assert_face_for_direction(Direction.FRONT, Direction.UP)
        self.assert_face_for_direction(Direction.BACK, Direction.DOWN)

    def test_b1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.BACK, 1))

        self.assert_face_for_direction(Direction.UP, Direction.RIGHT)
        self.assert_face_for_direction(Direction.RIGHT, Direction.DOWN)
        self.assert_face_for_direction(Direction.DOWN, Direction.LEFT)
        self.assert_face_for_direction(Direction.LEFT, Direction.UP)
        self.assert_face_for_direction(Direction.FRONT, Direction.FRONT)
        self.assert_face_for_direction(Direction.BACK, Direction.BACK)

    def test_b2_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.BACK, 2))

        self.assert_face_for_direction(Direction.UP, Direction.DOWN)
        self.assert_face_for_direction(Direction.RIGHT, Direction.LEFT)
        self.assert_face_for_direction(Direction.DOWN, Direction.UP)
        self.assert_face_for_direction(Direction.LEFT, Direction.RIGHT)
        self.assert_face_for_direction(Direction.FRONT, Direction.FRONT)
        self.assert_face_for_direction(Direction.BACK, Direction.BACK)

    def test_b_minus_1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.BACK, -1))

        self.assert_face_for_direction(Direction.UP, Direction.LEFT)
        self.assert_face_for_direction(Direction.RIGHT, Direction.UP)
        self.assert_face_for_direction(Direction.DOWN, Direction.RIGHT)
        self.assert_face_for_direction(Direction.LEFT, Direction.DOWN)
        self.assert_face_for_direction(Direction.FRONT, Direction.FRONT)
        self.assert_face_for_direction(Direction.BACK, Direction.BACK)

    def test_d1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.DOWN, 1))

        self.assert_face_for_direction(Direction.UP, Direction.UP)
        self.assert_face_for_direction(Direction.RIGHT, Direction.FRONT)
        self.assert_face_for_direction(Direction.DOWN, Direction.DOWN)
        self.assert_face_for_direction(Direction.LEFT, Direction.BACK)
        self.assert_face_for_direction(Direction.FRONT, Direction.LEFT)
        self.assert_face_for_direction(Direction.BACK, Direction.RIGHT)

    def test_d2_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.DOWN, 2))

        self.assert_face_for_direction(Direction.UP, Direction.UP)
        self.assert_face_for_direction(Direction.RIGHT, Direction.LEFT)
        self.assert_face_for_direction(Direction.DOWN, Direction.DOWN)
        self.assert_face_for_direction(Direction.LEFT, Direction.RIGHT)
        self.assert_face_for_direction(Direction.FRONT, Direction.BACK)
        self.assert_face_for_direction(Direction.BACK, Direction.FRONT)


    def test_d_minus_1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.DOWN, -1))

        self.assert_face_for_direction(Direction.UP, Direction.UP)
        self.assert_face_for_direction(Direction.RIGHT, Direction.BACK)
        self.assert_face_for_direction(Direction.DOWN, Direction.DOWN)
        self.assert_face_for_direction(Direction.LEFT, Direction.FRONT)
        self.assert_face_for_direction(Direction.FRONT, Direction.RIGHT)
        self.assert_face_for_direction(Direction.BACK, Direction.LEFT)

    def test_l1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.LEFT, 1))

        self.assert_face_for_direction(Direction.UP, Direction.BACK)
        self.assert_face_for_direction(Direction.RIGHT, Direction.RIGHT)
        self.assert_face_for_direction(Direction.DOWN, Direction.FRONT)
        self.assert_face_for_direction(Direction.LEFT, Direction.LEFT)
        self.assert_face_for_direction(Direction.FRONT, Direction.UP)
        self.assert_face_for_direction(Direction.BACK, Direction.DOWN)

    def test_l2_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.LEFT, 2))

        self.assert_face_for_direction(Direction.UP, Direction.DOWN)
        self.assert_face_for_direction(Direction.RIGHT, Direction.RIGHT)
        self.assert_face_for_direction(Direction.DOWN, Direction.UP)
        self.assert_face_for_direction(Direction.LEFT, Direction.LEFT)
        self.assert_face_for_direction(Direction.FRONT, Direction.BACK)
        self.assert_face_for_direction(Direction.BACK, Direction.FRONT)

    def test_l_minus_1_move_applied_correctly(self):
        self.orientation.change(Rotation(Direction.LEFT, -1))

        self.assert_face_for_direction(Direction.UP, Direction.FRONT)
        self.assert_face_for_direction(Direction.RIGHT, Direction.RIGHT)
        self.assert_face_for_direction(Direction.DOWN, Direction.BACK)
        self.assert_face_for_direction(Direction.LEFT, Direction.LEFT)
        self.assert_face_for_direction(Direction.FRONT, Direction.DOWN)
        self.assert_face_for_direction(Direction.BACK, Direction.UP)

    def test_ru_moves_applied_correctly(self):
        self.orientation.change(Rotation(Direction.RIGHT, 1))
        self.orientation.change(Rotation(Direction.UP, 1))

        self.assert_face_for_direction(Direction.UP, Direction.FRONT)
        self.assert_face_for_direction(Direction.RIGHT, Direction.UP)
        self.assert_face_for_direction(Direction.DOWN, Direction.BACK)
        self.assert_face_for_direction(Direction.LEFT, Direction.DOWN)
        self.assert_face_for_direction(Direction.FRONT, Direction.RIGHT)
        self.assert_face_for_direction(Direction.BACK, Direction.LEFT)

