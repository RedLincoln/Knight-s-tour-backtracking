"""GUI, Window of the board"""

import tkinter as tk
import itertools
from Cell import Cell


class GUI(tk.Tk):
    """Window where all the cells are going to be paint"""

    colors = ["White", "Black", "Black", "White"]
    color = itertools.cycle(colors)
    cells = []

    def __init__(self, title="Knight's tour", dimension=8):
        """

        :param title: title of the window
        :param dimension: dimension of the board
        """
        super(GUI, self).__init__()
        self.title(title)
        self.dimension = dimension;
        self.setup_cells()
        self.update_idletasks()

    def setup_cells(self):
        """create the cells and add them to the window"""
        for i in range(self.dimension):
            for j in range(self.dimension):
                cell = Cell(background_color=next(self.color)
                            , foreground_color=next(self.color))
                cell.grid(row=i, column=j, padx=2, pady=2)
                self.cells.append(cell)
            if self.dimension % 2 == 0:
                next(self.color)
                next(self.color)

    def set_cell_status(self, row, col, status, text):
        """to change the status of a cell in the board"""
        cell = self.cells[row * self.dimension + col]
        cell.update_cell(status, text=text)
