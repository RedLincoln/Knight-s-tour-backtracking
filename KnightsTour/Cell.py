"""
module for personalized labels used in the gui

:_selected_color: background color used when the cell is selected
:_width: width of the cell. one char -> one width
:_height: height of the cell. one char -> one height
"""

import tkinter as tk

_selected_color = "Green"
_width = 8
_height = 4


class Cell(tk.Label):
    """
    label used in the gui
    """

    def __init__(self, foreground_color="Black", background_color="White"):
        """

        :param foreground_color: text color
        :param background_color: background color
        """
        super(Cell, self).__init__()
        self.foreground_color = foreground_color
        self.background_color = background_color
        self.config(foreground=foreground_color, background=background_color
                    , width=_width, height=_height)
        self.update_idletasks()

    def update_cell(self, selected, text=None):
        """
        update the cell state and text

        :param selected: set if the cell if selected
        :param text: text to display if the cell is selected
        """
        if selected:
            self.config(background=_selected_color, text=text)
        else:
            self.config(background=self.background_color)
            self.config(text="")
        self.update_idletasks()
