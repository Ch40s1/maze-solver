from graphics import Window, Line, Point


def main():
    # create instance of window class
    win = Window(800, 800)
    # create an a line instance and then use x and y of
    # point isinstance to draw the line
    l = Line(Point(50, 50), Point(400, 400))
    win.draw_line(l, "blue")
    win.wait_for_close()


main()
