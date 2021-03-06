from cube import Cube
from direction import Direction
from move import Move
from renderer import ConsoleRenderer
from shuffler import Shuffler

if __name__ == '__main__':
    renderer = ConsoleRenderer()
    shuffler = Shuffler()

    c = Cube(3)
    print(shuffler.shuffle(c))
    # c.sequence('R2 L2 U2 D2 F2 B2')
    # c.sequence('R L- F- B U- D R L-')
    # c.sequence("F L F U' R U F2 L2 U' L' B D' B' L2 U")
    # c.sequence('S2 E2 M2')
    # renderer.render(c)
    # c.sequence("R2 L' D F2 R' D' R' L U' D R D B2 R' U D2")

    renderer.render(c)

