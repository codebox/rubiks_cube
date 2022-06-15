from direction import Direction


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
