from cube import Cube,  Group, Direction

if __name__ == '__main__':
    c = Cube(3)
    c.print()
    c.move(Direction.RIGHT, 1)
    c.move(Direction.LEFT, -1)
    c.move(Direction.UP, 1)
    c.move(Direction.DOWN, -1)
    c.move(Direction.FRONT, -1)
    c.move(Direction.BACK, 1)
    c.move(Direction.RIGHT, 1)
    c.move(Direction.LEFT, -1)
    c.print()
