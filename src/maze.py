from cell import Cell
import time
# maze class init


class Maze:

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        # for i in range of the number of columns
        for i in range(self._num_cols):
            # amke a colum cell list
            col_cells = []
            # for i in range of number of rows
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            # append to instance variable so we can use on other methods
            self._cells.append(col_cells)
        # this loops are just to get the indecies
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        # calculate the postion of the cell
        if self._win is None:
            return
        # calculate the postion of the cell at the indecies
        # staring from the position of the maze with add
        # the offset of the cell size by the index
        x1 = self._x1 + i * self._cell_size_x
        # then we do the same but from the top
        y1 = self._y1 + j * self._cell_size_y
        # once we have the top left corner with find the bottom right corner
        # we just add the cell to its coresponding dimension
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        # we then call the cells draw method
        self._cells[i][j].draw(x1, y1, x2, y2)
        # really we are done and dont need animate but it will let us visualy see it

    def _animate(self):
        if self._win is None:
            return
        # calls the redraw method to redo the last draw but with the sleep timer
        self._win.redraw()
        time.sleep(0.05)
