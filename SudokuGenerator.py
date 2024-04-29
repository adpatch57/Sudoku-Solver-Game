import random
import copy
from abc import ABC, abstractmethod
import Img


class Board:
    @abstractmethod
    def print_board(self):
        pass


class SudokuBoard(Board):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SudokuBoard, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.board = []
        self.solvedboard = []
        #self.generateBoard()
        self.removeNumbers = self.decorator(self.removeNumbers)
        self.removeNumbers()

    def print_board(self):
        print("Actual board :\n")
        print('+---------+---------+---------+')
        for i in range(9):
            line = "|"
            for j in range(9):
                line += f" {self.board[i][j]} "
                if (1 + j) % 3 == 0:
                    line += "|"
            print(line)
            if (1 + i) % 3 == 0:
                print('+---------+---------+---------+')

        print("Solved board :\n")

        print('+---------+---------+---------+')
        for i in range(9):
            line = "|"
            for j in range(9):
                line += f" {self.solvedboard[i][j]} "
                if (1 + j) % 3 == 0:
                    line += "|"
            print(line)
            if (1 + i) % 3 == 0:
                print('+---------+---------+---------+')

    def findSpaces(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col

        return False

    def checkSpace(self, num, pos):
        if not self.board[pos[0]][pos[1]] == 0:
            return False

        for col in self.board[pos[0]]:
            if col == num:
                return False

        for row in range(9):
            if self.board[row][pos[1]] == num:
                return False

        _internalBoxRow = pos[0] // 3
        _internalBoxCol = pos[1] // 3

        for i in range(3):  # check to see if internal box already has number
            for j in range(3):
                if self.board[i + (_internalBoxRow * 3)][j + (_internalBoxCol * 3)] == num:
                    return False

        return True

    def generateDiagonalFilledBoard(self):
        _l = list(range(1, 10))
        for row in range(3):
            for col in range(3):
                _num = random.choice(_l)
                self.board[row][col] = _num
                _l.remove(_num)

        _l = list(range(1, 10))
        for row in range(3, 6):
            for col in range(3, 6):
                _num = random.choice(_l)
                self.board[row][col] = _num
                _l.remove(_num)

        _l = list(range(1, 10))
        for row in range(6, 9):
            for col in range(6, 9):
                _num = random.choice(_l)
                self.board[row][col] = _num
                _l.remove(_num)

        return self.generateCompleteBoard()

    def generateCompleteBoard(self):  # uses recursion to finish generating a random board
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    num = random.randint(1, 9)

                    if self.checkSpace(num, (row, col)):
                        self.board[row][col] = num

                        if self.solve():
                            self.generateCompleteBoard()
                            return self.board

                        self.board[row][col] = 0

        return False

    def solve(self):
        positionAvailable = self.findSpaces()

        if not positionAvailable:
            return True
        else:
            row, col = positionAvailable

        for n in range(1, 10):
            if self.checkSpace(n, (row, col)):
                self.board[row][col] = n

                if self.solve():
                    return self.board

                self.board[row][col] = 0

        return False

    def is_valid(self, board, row, col, num):
        # Check if the number is already in the current row
        if num in board[row]:
            return False

        # Check if the number is already in the current column
        for i in range(9):
            if board[i][col] == num:
                return False

        # Check if the number is already in the current 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False

        return True

    def solve_sudoku(self, board):
        empty_cell = self.find_empty_cell(board)
        if not empty_cell:
            return True  # Board is already solved

        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid(board, row, col, num):
                board[row][col] = num
                if self.solve_sudoku(board):
                    return True
                board[row][col] = 0  # Backtrack if solution is not valid
        return False

    def find_empty_cell(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def count_sudoku_solutions(self, board):
        empty_cell = self.find_empty_cell(board)
        if not empty_cell:
            return 1  # Board is already solved

        count = 0
        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid(board, row, col, num):
                board[row][col] = num
                count += self.count_sudoku_solutions(board)
                board[row][col] = 0  # Backtrack
        return count

    def decorator(self, func):
        def generateBoard():
            self.board = [[0 for i in range(9)] for j in range(9)]
            self.generateDiagonalFilledBoard()
            self.solvedboard = copy.deepcopy(self.board)

            func()
        return generateBoard

    def removeNumbers(self):
        attempts = 5
        while attempts > 0:
            # Select a random cell that is not already empty
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while self.board[row][col] == 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
            # Remember its cell value in case we need to put it back
            backup = self.board[row][col]
            self.board[row][col] = 0

            # Take a full copy of the grid
            copyGrid = copy.deepcopy(self.board)

            # Count the number of solutions that this grid has (using a backtracking approach implemented in the solveGrid() function)
            solution_count = self.count_sudoku_solutions(copyGrid)
            # If the number of solution is different from 1 then we need to cancel the change by putting the value we took away back in the grid
            if solution_count != 1:
                self.board[row][col] = backup
                # We could stop here, but we can also have another attempt with a different cell just to try to remove more numbers
                attempts -= 1


    """
    def generateBoard(self):
        self.board = [[0 for i in range(9)] for j in range(9)]
        self.generateDiagonalFilledBoard()
        self.solvedboard = copy.deepcopy(self.board)

        self.removeNumbers()
    """







# mac = Board()
# mac.print_board()
