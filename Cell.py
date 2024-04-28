import tkinter as tk


class Cell:
    def __init__(self, board_grid):
        self.cell = tk.Button(board_grid, text='0', width=3, bg="#42a1f5", command=lambda: self.change_text())

    def change_text(self):
        if self.cell.cget('text') == ' ' or int(self.cell.cget('text')) == 9:
            self.cell.config(text='1')
        else:
            self.cell.config(text=((int(self.cell.cget('text'))) + 1) % 10)
