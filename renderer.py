from cube import Direction

class ConsoleRenderer:
    def render(self, cube):
        def face_grid(direction, get_x_coord, get_y_coord):
            grid = {}
            for piece in self._get_pieces_for_face(cube, direction):
                grid_x = get_x_coord(piece.coords)
                grid_y = get_y_coord(piece.coords)
                piece_face_value = piece.face_value(direction)
                grid[(grid_x, grid_y)] = piece_face_value

            return grid

        def coord_transformer(i, negate=False):
            if negate:
                return lambda c: (cube.size - 1) - (c[i] - cube.start_coord - (1 if not cube.is_odd and c[i] > 0 else 0))
            else:
                return lambda c: (c[i] - cube.start_coord - (1 if not cube.is_odd and c[i] > 0 else 0))

        u_grid = face_grid(Direction.UP, coord_transformer(0), coord_transformer(2))
        f_grid = face_grid(Direction.FRONT, coord_transformer(0), coord_transformer(1, True))
        l_grid = face_grid(Direction.LEFT, coord_transformer(2), coord_transformer(1, True))
        r_grid = face_grid(Direction.RIGHT, coord_transformer(2, True), coord_transformer(1, True))
        d_grid = face_grid(Direction.DOWN, coord_transformer(0), coord_transformer(2, True))
        b_grid = face_grid(Direction.BACK, coord_transformer(0), coord_transformer(1))

        full_grid = {}
        def add_to_full_grid(face_grid, x_offset, y_offset):
            for face_grid_coord, face_value in face_grid.items():
                full_grid[(face_grid_coord[0] + x_offset, face_grid_coord[1] + y_offset)] = face_value

        add_to_full_grid(u_grid, cube.size, 0)
        add_to_full_grid(l_grid, 0, cube.size)
        add_to_full_grid(f_grid, cube.size, cube.size)
        add_to_full_grid(r_grid, cube.size * 2, cube.size)
        add_to_full_grid(d_grid, cube.size, cube.size * 2)
        add_to_full_grid(b_grid, cube.size, cube.size * 3)

        grid_txt = ''
        # see https://stackoverflow.com/questions/38522909/how-to-print-color-box-on-the-console-in-python
        TEMPLATE = '\033[48;5;{}m'
        COLOUR_RED = TEMPLATE.format(160)
        COLOUR_YELLOW = TEMPLATE.format(226)
        COLOUR_ORANGE = TEMPLATE.format(202)
        COLOUR_WHITE = TEMPLATE.format(15)
        COLOUR_BLUE = TEMPLATE.format(12)
        COLOUR_GREEN = TEMPLATE.format(10)
        RESET_COLOUR = '\033[0;0m'
        colour_lookup = {
            Direction.UP: COLOUR_BLUE,
            Direction.DOWN: COLOUR_GREEN,
            Direction.RIGHT: COLOUR_RED,
            Direction.LEFT: COLOUR_ORANGE,
            Direction.FRONT: COLOUR_WHITE,
            Direction.BACK: COLOUR_YELLOW,
        }
        space = '  '
        for y in range(0, cube.size * 4):
            for x in range(0, cube.size * 3):
                c = (x,y)
                if c in full_grid:
                    face_value = full_grid[c]
                    face_colour = colour_lookup[face_value] + space + RESET_COLOUR + ' '
                    grid_txt += face_colour
                else:
                    grid_txt += RESET_COLOUR + space + ' '
            grid_txt += '\n'

        print(grid_txt)
        print(RESET_COLOUR)

    def _get_pieces_for_face(self, cube, face):
        coord_filter = {
            Direction.UP: lambda x, y, z: y == cube.end_coord - 1,
            Direction.DOWN: lambda x, y, z: y == cube.start_coord,
            Direction.LEFT: lambda x, y, z: x == cube.start_coord,
            Direction.RIGHT: lambda x, y, z: x == cube.end_coord - 1,
            Direction.FRONT: lambda x, y, z: z == cube.end_coord - 1,
            Direction.BACK: lambda x, y, z: z == cube.start_coord
        }.get(face)

        return [piece for piece in cube.pieces if coord_filter(*piece.coords)]
