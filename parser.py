import re

from direction import Direction
from move import Move
from math import trunc


class SequenceParser:
    parse_step_regex = re.compile('^(?P<face>[UDFBLR])(?P<count>[-2\']?)$')

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
            return Move([self.outer_slice_number], Direction(match['face']), count)

        else:
            raise ValueError('Unable to parse step: {}'.format(step_text))