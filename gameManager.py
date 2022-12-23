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
        self.board_array = np.zeros((self.board_size, self.board_size))
        print(self.board_array)
        self.white_turn = False

    def addUpdateUICallback(self, updateUiMethod):
        updateUiMethod()

    def cellPressed(self, x, y):
        self.board_array[y][x] = 1 if self.white_turn else 2
        print(self.board_array)

        liberties = np.zeros((self.board_size, self.board_size))
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                if not j-1 < 0:
                    if not self.board_array[i][j] == 0:
                        if self.board_array[i][j-1] == 0 or self.board_array[i][j-1] == self.board_array[i][j]:
                            liberties[i][j] += 1
                if not j+1 >= self.board_size:
                    if not self.board_array[i][j] == 0:
                        if self.board_array[i][j+1] == 0 or self.board_array[i][j+1] == self.board_array[i][j]:
                            liberties[i][j] += 1
                if not i-1 < 0:
                    if not self.board_array[i][j] == 0:
                        if self.board_array[i-1][j] == 0 or self.board_array[i-1][j] == self.board_array[i][j]:
                            liberties[i][j] += 1
                if not i+1 >= self.board_size:
                    if not self.board_array[i][j] == 0:
                        if self.board_array[i+1][j] == 0 or self.board_array[i+1][j] == self.board_array[i][j]:
                            liberties[i][j] += 1

        print(liberties)

        self.white_turn = not self.white_turn
