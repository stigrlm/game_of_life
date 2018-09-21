import os # to clear command line output and determine which command to use based on os
import numpy as np # numpy array serves as base grid for storing cell objects
from random import uniform # for determining random initial state
from cells import Cell # custom cell object

class World:
    def __init__(self, side_size, cell_alive_chance, cell_alive_mark='o'):
        self.side_size = side_size
        self.cell_alive_mark = cell_alive_mark
        self.cells = self.create_world(cell_alive_chance)
        self.cells_inner = self.cells[1:-1, 1:-1]

    def create_world(self, cell_alive_chance):
        # create empty array with size+2 width as outer rim will be needed to
        # simulate toroid structure
        cells = np.empty([self.side_size+2, self.side_size+2], dtype=object)
        # reference inner cells
        cells_inner = cells[1:-1, 1:-1]
        # populate inner array with cell objects and maked them alive/dead
        # based on random chance specified
        for i, cell_row in enumerate(cells_inner):
            for j, cell in enumerate(cell_row):
                cells_inner[i, j] = Cell(self._set_initial_cell_state(cell_alive_chance))

        # make mapping of outer cells to simulate toroid structure
        # e.g. same cell object will on be position 0,0 and 10,10 if 10 was selected as side_size
        for i in range(self.side_size):
            # setting top outer row
            cells[0, i+1] = cells_inner[-1, i]
            # setting left outer column
            cells[i+1, 0] = cells_inner[i, -1]
            # setting bottom outer row
            cells[-1, i+1] = cells_inner[0, i]
            # setting right outer column
            cells[i+1, -1] = cells_inner[i, 0]

        # setting corner cells_inner
        cells[0, 0] = cells_inner[-1, -1]
        cells[0, -1] = cells_inner[-1, 0]
        cells[-1, 0] = cells_inner[0, -1]
        cells[-1, -1] = cells_inner[0, 0]

        return cells

    def _set_initial_cell_state(self, cell_alive_chance):
        if uniform(0.0, 1.0) < cell_alive_chance:
            return True
        return False

    def display_world(self):
        cls_cmd_map = {'nt': 'cls',
                       'posix': 'clear'}

        os.system(cls_cmd_map[os.name])

        for cell_row in self.cells_inner:
            cell_marks = [self.cell_alive_mark if cell.alive_current else ' ' for cell in cell_row]
            print(' '.join(cell_marks))

    def resolve_cells(self):
        # pick neighbourhood for each cell
        # count alive neigbours and set alive_next
        # once done set alive_next for each cell to alive _current and set alive_next to None
        for i, cell_row in enumerate(self.cells_inner):
            for j, cell in enumerate(cell_row):
                neighbourhood = self.get_cell_neighbourhood(i+1, j+1)
                alive_neigbour_count = self.get_alive_neigbour_count(neighbourhood, cell)
                self.update_cell(alive_neigbour_count, cell)

    def update_round(self):
        for cell_row in self.cells_inner:
            for cell in cell_row:
                cell.set_alive_current(cell.alive_next)
                cell.set_alive_next(False)

    def update_cell(self, alive_neigbour_count, cell):
        if cell.alive_current:
            if alive_neigbour_count < 2 or alive_neigbour_count > 3 :
                cell.set_alive_next(False)
            else:
                cell.set_alive_next(True)
        else:
            if alive_neigbour_count == 3:
                cell.set_alive_next(True)
            else:
                cell.set_alive_next(False)

    def get_alive_neigbour_count(self, neighbourhood, current_cell):
        return np.sum(neighbourhood) - current_cell.alive_current

    def get_cell_neighbourhood(self, row, col):
        x1 = row - 1
        y1 = row + 2
        x2 = col - 1
        y2 = col + 2

        return self.cells[x1:y1, x2:y2]
