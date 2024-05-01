from graphics import Window, Line, Point
from cell import Cell


def main():
    # create instance of window class
    win = Window(800, 800)

    c1 = Cell(win)
    c1.has_left_wall = False
    c1.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.has_right_wall = False
    c2.draw(125, 125, 200, 200)

    # c = Cell(win)
    # c.has_bottom_wall = False
    # c.draw(225, 225, 250, 250)

    # c = Cell(win)
    # c.has_top_wall = False
    # c.draw(300, 300, 500, 500)

    # call draw_move from c1.draw_move(c2, undo=False)
    c1.draw_move(c2, True)

    win.wait_for_close()


main()
