from cell import Cell
import time
import random
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
        seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows -
                                        1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            destinations = []
            # check for top neighbor
            if j > 0 and not self._cells[i][j - 1].visited:
                destinations.append((i, j - 1))
            # check for right neighbor
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                destinations.append((i + 1, j))
            # check for bottom neighbor
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                destinations.append((i, j + 1))
            # check for left neighbor
            if i > 0 and not self._cells[i - 1][j].visited:
                destinations.append((i - 1, j))

            # check for zero directions
            if not destinations:
                break
            # pick rnadom direction
            next_i, next_j = random.choice(destinations)

            # break wall
            # i is cols j is rows
            # check if top wall
            if i == next_i and next_j < j:
                self._cells[i][j].has_top_wall = False
                self._draw_cell(i, j)
                self._cells[next_i][next_j].has_bottom_wall = False
                self._draw_cell(next_i, next_j)
            # check if right wall
            if j == next_j and next_i > i:
                self._cells[i][j].has_right_wall = False
                self._draw_cell(i, j)
                self._cells[next_i][next_j].has_left_wall = False
                self._draw_cell(next_i, next_j)
            # check if bottom wall
            if i == next_i and next_j > j:
                self._cells[i][j].has_bottom_wall = False
                self._draw_cell(i, j)
                self._cells[next_i][next_j].has_top_wall = False
                self._draw_cell(next_i, next_j)

            # check if left wall
            if j == next_j and next_i < i:
                self._cells[i][j].has_left_wall = False
                self._draw_cell(i, j)
                self._cells[next_i][next_j].has_right_wall = False
                self._draw_cell(next_i, next_j)

            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
