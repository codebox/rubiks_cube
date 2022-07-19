from direction import Direction
from random import choice
from move import Move


class Shuffler:
    def __init__(self):
        self.directions = [d for d in Direction]
        self.counts = [-1, 1, 2]
        self.direction_pairs = ((Direction.UP, Direction.DOWN), (Direction.LEFT, Direction.RIGHT), (Direction.FRONT, Direction.BACK))

    def _random_direction(self, excluding=[]):
        return choice([d for d in self.directions if d not in excluding])

    def _random_count(self):
        return choice(self.counts)

    def _random_slice(self, cube):
        return choice([s for s in range(cube.start_coord, cube.end_coord) if s != 0 or cube.is_odd])

    def _directions_to_exclude(self, last_direction):
        return next((pair for pair in self.direction_pairs if last_direction in pair), [])

    def shuffle(self, cube, move_count=20):
        moves = []
        for _ in range(move_count):
            directions_to_exclude = self._directions_to_exclude(moves[-1].direction) if moves else []
            move = Move([self._random_slice(cube)], self._random_direction(directions_to_exclude), self._random_count())
            moves.append(move)
            cube.move(move)

        return moves