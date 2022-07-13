from direction import Direction
from random import choice
from move import Move


class Shuffler:
    def __init__(self):
        self.directions = [d for d in Direction]
        self.counts = [-1, 1, 2]

    def _random_direction(self):
        return choice(self.directions)

    def _random_count(self):
        return choice(self.counts)

    def _random_slice(self, cube):
        return choice([s for s in range(cube.start_coord, cube.end_coord) if s != 0 or cube.is_odd])

    def _random_move(self, cube):
        return Move([self._random_slice(cube)], self._random_direction(), self._random_count())

    def shuffle(self, cube, move_count=20):
        moves = []
        for _ in range(move_count):
            move = self._random_move(cube)
            moves.append(move)
            cube.move(move)

        return moves