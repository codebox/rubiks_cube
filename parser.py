import re

from direction import Direction
from move import Move
from math import trunc


class SequenceParser:
    parse_step_regex = re.compile('^(?P<face>[UDFBLRMESxyzXYZ])(?P<count>[-2\']?)$')

    def __init__(self, cube_size):
        self.cube_size = cube_size
        self.outer_slice_number = trunc(cube_size/2)

    def parse_sequence(self, sequence_text):
        return [self._parse_step(step_text) for step_text in sequence_text.split()]

    def _parse_step(self, step_text):
        match = SequenceParser.parse_step_regex.search(step_text)

        if match:
            count_txt = match['count']
            count = {
                "2": 2,
                "-": -1,
                "'": -1
            }.get(count_txt, 1)

            face_txt = match['face']
            all_slices = [s for s in range(-self.outer_slice_number, self.outer_slice_number + 1) if s != 0 or self.cube_size % 2 == 1]
            direction, slice_number = {
                'U': (Direction.UP, [self.outer_slice_number]),
                'D': (Direction.DOWN, [self.outer_slice_number]),
                'L': (Direction.LEFT, [self.outer_slice_number]),
                'R': (Direction.RIGHT, [self.outer_slice_number]),
                'F': (Direction.FRONT, [self.outer_slice_number]),
                'B': (Direction.BACK, [self.outer_slice_number]),
                'M': (Direction.LEFT, [0]),
                'E': (Direction.DOWN, [0]),
                'S': (Direction.FRONT, [0]),
                'x': (Direction.RIGHT, all_slices),
                'X': (Direction.RIGHT, all_slices),
                'y': (Direction.UP, all_slices),
                'Y': (Direction.UP, all_slices),
                'z': (Direction.FRONT, all_slices),
                'Z': (Direction.FRONT, all_slices)
            }.get(face_txt)

            return Move(slice_number, direction, count)

        else:
            raise ValueError('Unable to parse step: {}'.format(step_text))
