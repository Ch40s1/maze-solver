from tkinter import Tk, BOTH, Canvas


class Window:

    # constructor
    def __init__(self, width, height):
        # create tkinter window
        self.__root = Tk()
        # set the window title
        self.__root.title("Maze Solver")
        # edit the window
        self.__canvas = Canvas(self.__root, bg="white",
                               width=width, height=height)
        # pack it so it is ready to be drawn
        self.__canvas.pack(fill=BOTH, expand=True)
        # set window running to false
        self.__running = False
        # call the self.close when we close the window
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    # redraw calls update_idletasks and update on window
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    # set runnign to true

    def wait_for_close(self):
        self.__running = True
        print("window is running...")
        # while running call redraw
        while self.__running:
            self.redraw()
        print("window closed")

    # close sets running to false
    def close(self):
        self.__running = False

# create a point class that stores location of the points


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

# create a class that uses the points and draws a line connecting them


class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Cell:

    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def remove_top_wall(self):
        self.has_top_wall = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
