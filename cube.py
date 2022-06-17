from math import trunc

from parser import SequenceParser
from direction import Direction
from piece import Piece
from rotation import Rotation


class Cube:
    def __init__(self, size=3):
        if size < 1:
            raise ValueError("Invalid size: {}".format(size))
        self.size = size
        self.is_odd = self.size % 2 == 1
        self.start_coord = -trunc(self.size/2)
        self.end_coord = -self.start_coord
        self.pieces = self._init_pieces()
        self.parser = SequenceParser(size)

    def _init_pieces(self):
        return [
            Piece((x, y, z))
            for x in range(self.start_coord, self.end_coord + 1) if self.is_odd or x != 0
            for y in range(self.start_coord, self.end_coord + 1) if self.is_odd or y != 0
            for z in range(self.start_coord, self.end_coord + 1) if (self.is_odd or z != 0) and (max(abs(x), abs(y), abs(z)) == self.end_coord)
        ]

    def get_pieces_for_face(self, face):
        return self._get_pieces_in_slice(face, trunc(self.size / 2))

    def _get_pieces_in_slice(self, direction, index):
        coord_filter = {
            Direction.UP: lambda x, y, z: y == index,
            Direction.DOWN: lambda x, y, z: -y == index,
            Direction.RIGHT: lambda x, y, z: x == index,
            Direction.LEFT: lambda x, y, z: -x == index,
            Direction.FRONT: lambda x, y, z: z == index,
            Direction.BACK: lambda x, y, z: -z == index
        }.get(direction)

        return [piece for piece in self.pieces if coord_filter(*piece.coords)]

    def sequence(self, sequence_text):
        [self.move(move) for move in self.parser.parse_sequence(sequence_text)]

    def move(self, move):
        if not move.is_valid_for_cube_size(self.size):
            raise ValueError('The move {} is not valid for a cube of size {}'.format(move, self.size))

        pieces_affected = [piece for piece in self.pieces if move.affects_piece(piece)]

        d = 1 if move.count > 0 else -1
        transform = {
            Direction.UP: lambda x, y, z: (-z*d, y, x*d),
            Direction.DOWN: lambda x, y, z: (z*d, y, -x*d),
            Direction.LEFT: lambda x, y, z: (x, -z*d, y*d),
            Direction.RIGHT: lambda x, y, z: (x, z*d, -y*d),
            Direction.FRONT: lambda x, y, z: (y*d, -x*d, z),
            Direction.BACK: lambda x, y, z: (-y*d, x*d, z)
        }.get(move.direction)

        rotation = Rotation(move.direction, move.count)
        for piece in pieces_affected:
            for _ in range(abs(move.count)):
                piece.move(transform(*piece.coords))
            piece.rotate(rotation)

    def is_done(self):
        def count_colours_on_face(face):
            return len(set([piece.face_value(face) for piece in self.get_pieces_for_face(face)]))
        return all(count_colours_on_face(direction) == 1 for direction in Direction)

