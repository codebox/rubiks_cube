from cube import Cube
from renderer import ConsoleRenderer

if __name__ == '__main__':
    renderer = ConsoleRenderer()
    c = Cube(3)
    renderer.render(c)
    print(c.is_done())

    c.move("F D R")
    print(c.is_done())

    c.move("R- D-")
    print(c.is_done())

    c.move("F-")
    print(c.is_done())

    # c.move('R2 L2 U2 D2 F2 B2')
    # c.move('R L- F- B U- D R L-')
    # c.move("F L F U' R U F2 L2 U' L' B D' B' L2 U")

    renderer.render(c)
