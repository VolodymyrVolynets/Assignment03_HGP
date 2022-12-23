import random

import numpy as np
class GameManager():
    """
    Кароче чел, эта хуйня генерит масив 7 ан 7 изначально там одни 0,
    когда кто то нажимает на ячейку выполняеться метод селлпресесд и рандомно генерит 1 или 2,
    1 это первый игрок, 2 это второй игрок
    добавил аптейт юа на всякий случай, по умолчанию юай обновляеться после нажатия на ячейку
    по сути у тебя есть масив доски self.board_array и есть то куда нажал юзер cellPressed(self, x, y):
    и ты долэен это обработать как то и поменять масив доски
    """

    def __init__(self, board_size):
        self.board_size = board_size
        self.board_array = np.zeros((board_size, board_size))
        self.player_one_move = True

    def addUpdateUICallback(self, updateUiMethod):
        updateUiMethod()

    def cellPressed(self, x, y):
        if not self.isAlreadyStonePlaced(x, y):
            self.board_array[x][y] = 1 if self.player_one_move else 2
            self.player_one_move = not self.player_one_move

        #Захватывает только если 1 камень окружен если их несколько то иди ты нахуй http://www.allaboutgo.com/play-go-9.html потестить как работает можно тут
        self.remove_surrounded_groups(self.board_array)

    def isAlreadyStonePlaced(self, x, y):
        return self.board_array[x][y] != 0

    def remove_surrounded_stones(self, board, x, y):
        # check if the position is out of bounds or not occupied by a stone
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] == 0:
            return False

        # check if the stone is surrounded on all sides
        if (x > 0 and board[x - 1][y] != board[x][y] and board[x - 1][y] != 0) and (x < len(board) - 1 and board[x + 1][y] != board[x][y] and board[x + 1][y] != 0) and (y > 0 and board[x][y - 1] != board[x][y] and board[x][y - 1] != 0) and (y < len(board[0]) - 1 and board[x][y + 1] != board[x][y] and board[x][y + 1] != 0):
            # remove the stone
            board[x][y] = 0
            return True

        else:
            return False


    def remove_surrounded_groups(self, board):
        # print(1)
        # keep track of whether any stones were removed
        removed = False

        # check each stone on the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.remove_surrounded_stones(board, i, j):
                    print(2)
                    removed = True

        # if any stones were removed, check for more surrounded groups
        if removed:
            self.remove_surrounded_groups(board)


