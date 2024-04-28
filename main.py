import tkinter as tk
from tkinter import font as tkfont
from tkinter import filedialog
from PIL import Image, ImageTk
import pyglet
import SudokuGenerator
import Cell
import Img

pyglet.font.add_file('mc.otf')


class SAMPLEAPP(tk.Tk):
    # Prototype Design Pattern
    def Type(self):
        return "Application"

    def __str__(self):
        return "APP"

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)  # this needed to be added
        self.grid_columnconfigure(0, weight=1)  # as did this
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, SolveItYourself, SolveFromImage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        """
        Show a frame for the given page name
        """
        frame = self.frames[page_name]
        frame.tkraise()


class MainMenu(tk.Frame):
    def Type(self):
        return "Main Menu"

    def __str__(self):
        return "MENU"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)  # as did this

        ctr_top = tk.Frame(self, height=700)
        ctr_top.grid_propagate(False)
        ctr_top.grid(row=0, sticky="ew")

        label = tk.Label(ctr_top, text="Sudoku Solver!", font=controller.title_font)
        label.grid(row=0, pady=(60, 0), padx=250)

        ctr_center = tk.Frame(ctr_top, height=500, width=100)
        ctr_center.grid_propagate(False)
        ctr_center.grid(row=1, sticky="ew", padx=200, pady=(30, 0))

        btn1_frame = tk.Frame(ctr_center, height=70, width=300)
        btn1_frame.grid_propagate(False)
        btn1_frame.grid(row=0, sticky="ew")

        btn2_frame = tk.Frame(ctr_center, height=70, width=300)
        btn2_frame.grid_propagate(False)
        btn2_frame.grid(row=1, sticky="ew", pady=(50, 0))

        btn3_frame = tk.Frame(ctr_center, height=70, width=300)
        btn3_frame.grid_propagate(False)
        btn3_frame.grid(row=2, sticky="ew", pady=(50, 0))

        button1 = tk.Button(btn1_frame, text="Solve it yourself!",
                            command=lambda: controller.show_frame("SolveItYourself"),
                            background='#a4a8b0', font=('Minecraft', 15), width=23, height=3)
        button2 = tk.Button(btn2_frame, text="Solve sudoku from image!", width=23, height=3,
                            command=lambda: controller.show_frame("SolveFromImage"),
                            background='#a4a8b0', font=('Minecraft', 15))

        button3 = tk.Button(btn3_frame, text="Quit", command=quit, background='#a4a8b0',
                            font=('Minecraft', 15), width=23, height=3)

        button1.grid()
        button2.grid()
        button3.grid()


class SolveItYourself(tk.Frame):
    def Type(self):
        return "SOLVE SUDOKU"

    def __str__(self):
        return "SIYS"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #####################################################################
        # Frames initialization
        #####################################################################

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        top_frame = tk.Frame(self, width=700, height=50)
        center = tk.Frame(self, width=700, height=450)

        top_frame.grid(row=0, sticky="ew")
        top_frame.grid_propagate(False)

        center.grid(row=1, sticky="nsew")
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)
        center.grid_propagate(False)

        ctr_left = tk.Frame(center, width=350, padx=3, pady=3)
        ctr_right = tk.Frame(center, width=350, padx=3, pady=3)

        ctr_left.grid(row=0, column=0, sticky="nsew")
        ctr_right.grid(row=0, column=1, sticky="nsew")
        ctr_left.grid_propagate(False)
        ctr_right.grid_propagate(False)

        #####################################################################
        # Content
        #####################################################################

        Backbutton = tk.Button(top_frame, text="BACK",
                               command=lambda: controller.show_frame("MainMenu"))
        Backbutton.grid(row=0, padx=3, pady=10, sticky="ns")

        label = tk.Label(top_frame, text="SOLVE SUDOKU YOURSELF!", font=controller.title_font)
        label.grid(pady=10, row=0, column=1, padx=130)

        ctr_left_top = tk.Frame(ctr_left, height=60)
        ctr_left_top.grid_propagate(False)
        ctr_left_top.grid(row=0, sticky="ew")

        ctr_right_top = tk.Frame(ctr_right, height=60)
        ctr_right_top.grid_propagate(False)
        ctr_right_top.grid(row=0, sticky="ew")

        board_grid = tk.Frame(ctr_left, bg='black', width=285, height=240)
        board_grid.grid_propagate(False)
        board_grid.grid(row=1, padx=30, pady=50)

        result_grid = tk.Frame(ctr_right, bg='black', width=285, height=240)
        result_grid.grid_propagate(False)
        result_grid.grid(row=1, padx=30, pady=50)

        self.sudoku = SudokuGenerator.SudokuBoard()
        self.board = self.sudoku.board
        self.solved_board = self.sudoku.solvedboard

        def generate_grid():
            self.sudoku = SudokuGenerator.SudokuBoard()
            self.sudoku.print_board()  # For debug
            self.board = self.sudoku.board
            self.result_board = self.sudoku.solvedboard

            buttons_list = []
            for k in range(81):
                buttons_list.append(Cell.Cell(board_grid))

            print(len(buttons_list))  # Debug

            for i in range(9):
                for j in range(9):
                    buttons_list[9 * i + j].cell.config(
                        text=f"{self.sudoku.board[i][j] if self.sudoku.board[i][j] != 0 else ' '}")
                    if buttons_list[9 * i + j].cell.cget('text') != ' ':
                        buttons_list[9 * i + j].cell.config(state='disabled', disabledforeground='black')
                    if buttons_list[9 * i + j].cell.cget('text') == ' ':
                        buttons_list[9 * i + j].cell.config(bg='white')

                    # Placing buttons on the grid
                    if i != 0 and j != 0 and i % 3 == 0 and j % 3 == 0:
                        buttons_list[9 * i + j].cell.grid(row=i, column=j, padx=(4, 0), pady=(4, 0))

                    elif j != 0 and j % 3 == 0:
                        buttons_list[9 * i + j].cell.grid(row=i, column=j, padx=(4, 0))

                    elif i != 0 and i % 3 == 0:
                        buttons_list[9 * i + j].cell.grid(row=i, column=j, pady=(4, 0))

                    else:
                        buttons_list[9 * i + j].cell.grid(row=i, column=j)

            return self.sudoku.board, self.sudoku.solvedboard

        def show_result():
            result_board = self.result_board
            buttons_list = []
            for k in range(81):
                buttons_list.append(Cell.Cell(result_grid))

            for i in range(9):
                for j in range(9):
                    buttons_list[9 * i + j].cell.config(
                        text=f"{result_board[i][j] if result_board[i][j] != 0 else ' '}")
                    if buttons_list[9 * i + j].cell.cget('text') != ' ':
                        buttons_list[9 * i + j].cell.config(state='disabled', disabledforeground='black')
                    if buttons_list[9 * i + j].cell.cget('text') == ' ':
                        buttons_list[9 * i + j].cell.config(bg='white')

                    # Placing buttons on the grid
                    if i != 0 and j != 0 and i % 3 == 0 and j % 3 == 0:
                        buttons_list[9 * i + j].cell.grid(row=i, column=j, padx=(4, 0), pady=(4, 0))

                    elif j != 0 and j % 3 == 0:
                        buttons_list[9 * i + j].cell.grid(row=i, column=j, padx=(4, 0))

                    elif i != 0 and i % 3 == 0:
                        buttons_list[9 * i + j].cell.grid(row=i, column=j, pady=(4, 0))

                    else:
                        buttons_list[9 * i + j].cell.grid(row=i, column=j)

        def saveAsImg():
            fileTypes = [("Image files", "*.png")]
            path = tk.filedialog.asksaveasfilename(filetypes=fileTypes)

            # if file is selected
            if len(path):
                boards = self.sudoku
                s = Img.SudokuImage()
                s.BoardToImage(boards.board, path)

            #   if no file is selected, then we are displaying below message
            else:
                print("No file is Choosen !! Please choose a file.")

        RegenerateButton = tk.Button(ctr_left_top, text="Regenerate", command=generate_grid)
        RegenerateButton.grid(row=0, column=0, pady=15, padx=30)
        ResultButton = tk.Button(ctr_left_top, text="Result", command=show_result)
        ResultButton.grid(row=0, column=1, padx=30, pady=15)
        generate_grid()

        SaveButton = tk.Button(ctr_right_top, text="Save", command=saveAsImg)
        SaveButton.grid(row=0, column=0, padx=30, pady=15)


class SolveFromImage(tk.Frame):
    def Type(self):
        return "SOLVE SUDOKU FROM IMAGE"

    def __str__(self):
        return "SSFI"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # self.img = ImageTk.PhotoImage(file='placeholder.png')
        self.image = Image.open('placeholder.png')

        #   Frames init
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        top_frame = tk.Frame(self, width=700, height=50)
        center = tk.Frame(self, width=700, height=450)

        top_frame.grid(row=0, sticky="ew")
        top_frame.grid_propagate(False)

        center.grid(row=1, sticky="nsew")
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)
        center.grid_propagate(False)

        ctr_left = tk.Frame(center, width=350, padx=3, pady=3)
        ctr_right = tk.Frame(center, width=350, padx=3, pady=3)

        ctr_left.grid(row=0, column=0, sticky="nsew")
        ctr_right.grid(row=0, column=1, sticky="nsew")
        ctr_left.grid_propagate(False)
        ctr_right.grid_propagate(False)

        #####################################################################
        # Content
        #####################################################################

        Backbutton = tk.Button(top_frame, text="BACK",
                               command=lambda: controller.show_frame("MainMenu"))
        Backbutton.grid(row=0, padx=3, pady=10, sticky="ns")

        label = tk.Label(top_frame, text="SOLVE SUDOKU FROM IMAGE!", font=controller.title_font)
        label.grid(pady=10, row=0, column=1, padx=130)

        ctr_left_top = tk.Frame(ctr_left, height=100, width=250)
        ctr_left_top.grid_propagate(False)
        ctr_left_top.grid(row=0, sticky="ew")

        label = tk.Label(ctr_left_top, text="Upload a sudoku picture and click on 'Solve' to solve it!")
        label.grid(pady=10, row=0, column=0, padx=10)

        buttonsframe = tk.Frame(ctr_left_top, height=50, width=250)
        buttonsframe.grid_propagate(False)
        buttonsframe.grid(row=1, sticky='nsew')

        Uploadbutton = tk.Button(buttonsframe, text="Upload",
                                 command=lambda: self.uploadImage())
        Uploadbutton.grid(row=0, column=0, padx=30, pady=10, sticky="ns")

        Solvebutton = tk.Button(buttonsframe, text="Solve",
                                command=lambda: self.solveImage())
        Solvebutton.grid(row=0, column=1, pady=10, sticky="ns")

        #   adding background image
        resized_image = self.image.resize((300, 300))
        img = ImageTk.PhotoImage(resized_image)
        self.image = img
        self.imgLabel = tk.Label(ctr_left, image=self.image)
        self.imgLabel.grid(row=1, pady=(30, 0), padx=(20, 0))

    def uploadImage(self):
        fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
        path = tk.filedialog.askopenfilename(filetypes=fileTypes)

        # if file is selected
        if len(path):
            img = Image.open(path)
            img = img.resize((300, 300))
            self.image = ImageTk.PhotoImage(img)
            self.imgLabel.config(image=self.image)

        #   if no file is selected, then we are displaying below message
        else:
            print("No file is Choosen !! Please choose a file.")

    def solveImage(self):
        pass


if __name__ == "__main__":
    app = SAMPLEAPP()
    app.title('Sudoku Solver')
    app.geometry('700x500')
    app.resizable(False, False)
    app.mainloop()
