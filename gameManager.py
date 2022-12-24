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
        self.prev_liberties = np.ones((self.board_size, self.board_size))
        print(self.board_array)
        self.white_turn = False
        self.board_array = np.zeros((board_size, board_size))

        self.black_score = 0
        self.black_player_stones_eaten = 0
        self.white_score = 0
        self.white_player_stones_eaten = 0

    def addUpdateUICallback(self, updateUiMethod):
        updateUiMethod()

    def cellPressed(self, x, y):

        # check if the move is valid
        if self.board_array[y][x] == 0:
            self.board_array[y][x] = 1 if self.white_turn else 2
            if self.getLiberties(y, x) == 0:
                self.board_array[y][x] = 0
                print("Invalid move")
                return
        else:
            print("Move not valid")
            return

        print(self.board_array)

        # get the liberties of each stone
        liberties = np.zeros((self.board_size, self.board_size))
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                liberties[i][j] = self.getLiberties(i, j)

        # chains = []
        # print(chains)
        #
        # for chain in chains:
        #     i = chain[0]
        #     j = chain[1]
        #     count = 0
        #     if not j - 1 < 0:
        #         if not self.board_array[i][j-1] == 0 and not self.board_array[i][j-1] == self.board_array[i][j]:
        #             count += 1
        #     if not j + 1 >= self.board_size:
        #         if not self.board_array[i][j+1] == 0 and not self.board_array[i][j+1] == self.board_array[i][j]:
        #             count += 1
        #     if not i - 1 < 0:
        #         if not self.board_array[i-1][j] == 0 and not self.board_array[i-1][j] == self.board_array[i][j]:
        #             count += 1
        #     if not i + 1 >= self.board_size:
        #         if not self.board_array[i+1][j] == 0 and not self.board_array[i+1][j] == self.board_array[i][j]:
        #             count += 1
        #
        #     if count == 4:
        #         liberties[i][j] = 0

        print(liberties)
        white_player_stones_eaten = 0
        black_player_stones_eaten = 0
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                if liberties[i][j] == 0:
                    if not self.board_array[i][j] == 0:
                        if self.white_turn:
                            white_player_stones_eaten += 1
                        else:
                            black_player_stones_eaten += 1
                    self.board_array[i][j] = 0
        print(white_player_stones_eaten)
        print(black_player_stones_eaten)

        # update score
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                if not liberties[i][j] == self.prev_liberties[i][j] and liberties[i][j] == 0:
                    if self.white_turn:
                        self.white_score += 1
                    else:
                        self.black_score += 1
                if not liberties[i][j] == self.prev_liberties[i][j] and self.prev_liberties[i][j] == 0:
                    if self.white_turn:
                        self.black_score -= 1
                    else:
                        self.white_score -= 1

        self.white_score += white_player_stones_eaten
        self.black_score += black_player_stones_eaten

        print(f"Black player score: {self.black_score}")
        print(f"White player score: {self.white_score}")

        self.prev_liberties = liberties
        self.white_turn = not self.white_turn

    def getLiberties(self, i, j):
        count = 0
        temp = self.board_array[i][j]
        if not j - 1 < 0:
            # if not self.board_array[i][j] == 0:
            if self.board_array[i][j - 1] == 0:
                count += 1
            elif self.board_array[i][j - 1] == self.board_array[i][j]:
                self.board_array[i][j] = 100
                count += self.getLiberties(i, j-1)
                self.board_array[i][j] = temp
        if not j + 1 >= self.board_size:
            # if not self.board_array[i][j] == 0:
            if self.board_array[i][j + 1] == 0:
                count += 1
            elif self.board_array[i][j + 1] == self.board_array[i][j]:
                self.board_array[i][j] = 101
                count += self.getLiberties(i, j+1)
                self.board_array[i][j] = temp
        if not i - 1 < 0:
            # if not self.board_array[i][j] == 0:
            if self.board_array[i - 1][j] == 0:
                count += 1
            elif self.board_array[i - 1][j] == self.board_array[i][j]:
                self.board_array[i][j] = 102
                count += self.getLiberties(i-1, j)
                self.board_array[i][j] = temp
        if not i + 1 >= self.board_size:
            # if not self.board_array[i][j] == 0:
            if self.board_array[i + 1][j] == 0:
                count += 1
            elif self.board_array[i + 1][j] == self.board_array[i][j]:
                self.board_array[i][j] = 103
                count += self.getLiberties(i+1, j)
                self.board_array[i][j] = temp

        return count


    def passTurn(self):
        self.white_turn = not self.white_turn
