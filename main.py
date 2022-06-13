from cube import Cube,  Group, Direction

if __name__ == '__main__':
    c = Cube(2)
    c.print()
    c.move(Direction.FRONT, 1)
    c.print()
    # print(Cube(2)._get_face_pieces(Direction.LEFT))
    # g = Group('u','r','d','l')
    # print(g.move_from('r', 17))