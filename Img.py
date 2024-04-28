from PIL import Image


class SudokuImage:
    def __init__(self):
        self.grid = Image.open('Images/grid.png')
        self.one = Image.open('Images/1.png')
        self.two = Image.open('Images/2.png')
        self.three = Image.open('Images/3.png')
        self.four = Image.open('Images/4.png')
        self.five = Image.open('Images/5.png')
        self.six = Image.open('Images/6.png')
        self.seven = Image.open('Images/7.png')
        self.eight = Image.open('Images/8.png')
        self.nine = Image.open('Images/9.png')
        self.none = Image.open('Images/0.png')

    def BoardToImage(self, board, path):
        board_img = self.grid.copy()
        x = 0
        y = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == 1:
                    board_img.paste(self.one, (x, y))
                    x = ((x + 95) % 860)
                elif board[i][j] == 2:
                    board_img.paste(self.two, (x, y))
                    x = ((x + 95) % 860)
                elif board[i][j] == 3:
                    board_img.paste(self.three, (x, y))
                    x = ((x + 95) % 860)
                elif board[i][j] == 4:
                    board_img.paste(self.four, (x, y))
                    x = ((x + 95) % 860)
                elif board[i][j] == 5:
                    board_img.paste(self.five, (x, y))
                    x = ((x + 95) % 860)
                elif board[i][j] == 6:
                    board_img.paste(self.six, (x, y))
                    x = ((x + 95) % 860)
                elif board[i][j] == 7:
                    board_img.paste(self.seven, (x, y))
                    x = ((x + 95) % 860)
                elif board[i][j] == 8:
                    board_img.paste(self.eight, (x, y))
                    x = ((x + 95) % 860)
                elif board[i][j] == 9:
                    board_img.paste(self.nine, (x, y))
                    x = ((x + 95) % 860)
                else:
                    board_img.paste(self.none, (x, y))
                    x = ((x + 95) % 860)
            x = 0
            y = ((y + 95) % 860)

        board_img.save(f'{path}.png')


#boards = SudokuGenerator.SudokuBoard()
#s = SudokuImage()
#boards.print_board()
#s.BoardToImage(boards.board)
