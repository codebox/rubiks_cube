from math import trunc
from parser import SequenceParser
from direction import Direction

class Rotation:
    def __init__(self, direction, count):
        self.direction = direction
        self.count = count % 4

    def __str__(self):
        return "{}{}".format(self.direction[0], self.count)


class Orientation:
    initial_face_directions = {
        Direction.FRONT: Direction.FRONT,
        Direction.BACK: Direction.BACK,
        Direction.RIGHT: Direction.RIGHT,
        Direction.LEFT: Direction.LEFT,
        Direction.UP: Direction.UP,
        Direction.DOWN: Direction.DOWN
    }

    class Group:
        def __init__(self, *members):
            self.members = list(members)

        def move_from(self, start_member, step_count):
            if start_member in self.members:
                return self.members[(self.members.index(start_member) + step_count) % len(self.members)]
            else:
                return start_member

    def __init__(self):
        self.direction_faces = dict(Orientation.initial_face_directions)

    rotation_groups = {
        Direction.RIGHT: Group(Direction.FRONT, Direction.UP, Direction.BACK, Direction.DOWN),
        Direction.LEFT: Group(Direction.BACK, Direction.UP, Direction.FRONT, Direction.DOWN),
        Direction.UP: Group(Direction.RIGHT, Direction.FRONT, Direction.LEFT, Direction.BACK),
        Direction.DOWN: Group(Direction.LEFT, Direction.FRONT, Direction.RIGHT, Direction.BACK),
        Direction.FRONT: Group(Direction.LEFT, Direction.UP, Direction.RIGHT, Direction.DOWN),
        Direction.BACK: Group(Direction.RIGHT, Direction.UP, Direction.LEFT, Direction.DOWN)
    }

    def change(self, rotation):
        rotation_group = Orientation.rotation_groups[rotation.direction]
        self.direction_faces = {rotation_group.move_from(direction, rotation.count): face
                                for direction, face in self.direction_faces.items()}

    def get_face_for_direction(self, direction):
        return self.direction_faces[direction]


class Piece:
    def __init__(self, initial_coords):
        self.id = "{},{},{}".format(*initial_coords)
        self.initial_coords = initial_coords
        self.coords = initial_coords
        self.orientation = Orientation()

    def move(self, new_coords):
        self.coords = new_coords

    def rotate(self, rotation):
        self.orientation.change(rotation)

    def face_value(self, direction):
        return self.orientation.get_face_for_direction(direction)

    def __str__(self):
        return "Piece[{}] {}".format(self.id, self.orientation)

    __repr__ = __str__


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

        for piece in pieces_affected:
            for _ in range(abs(move.count)):
                piece.move(transform(*piece.coords))

        [piece.rotate(Rotation(move.direction, move.count)) for piece in pieces_affected]

    def is_done(self):
        def check_piece(p,d): return p.orientation.get_face_for_direction(d) == d
        return all(all(check_piece(piece, direction) for piece in self.get_pieces_for_face(direction)) for direction in Direction)

    def __str__(self):
        return "{0}x{0} cube with {1} pieces {2}".format(self.size, len(self.pieces), self.pieces)
