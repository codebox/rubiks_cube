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
        self.end_coord = -self.start_coord + 1
        self.pieces = self._init_pieces()
        self.parser = SequenceParser(size)

    def _init_pieces(self):
        return [
            Piece((x, y, z))
            for x in range(self.start_coord, self.end_coord) if self.is_odd or x != 0
            for y in range(self.start_coord, self.end_coord) if self.is_odd or y != 0
            for z in range(self.start_coord, self.end_coord) if self.is_odd or z != 0
        ]

    def get_pieces_for_face(self, face):
        index = trunc(self.size / 2) * -1 if face in [Direction.LEFT, Direction.DOWN, Direction.BACK] else 1
        return self._get_pieces_in_slice(face, index)

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
        def check_piece(p,d): return p.orientation.get_face_for_direction(d) == d
        return all(all(check_piece(piece, direction) for piece in self.get_pieces_for_face(direction)) for direction in Direction)
