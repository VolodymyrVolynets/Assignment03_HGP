import random
import numpy as np

import dockWidget


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
        self.states = []
        self.prev_liberties = np.ones((self.board_size, self.board_size))
        print(self.board_array)
        self.buttonCount = 0
        self.white_turn = False
        self.board_array = np.zeros((board_size, board_size))

        self.black_score = 0
        self.black_player_stones_eaten = 0
        self.territory_controlled_by_black = 0
        self.white_score = 0
        self.white_player_stones_eaten = 0
        self.territory_controlled_by_white = 0
        self.update_dock_widget_ui = None
        self.info_label = ""
    def addUpdateUICallback(self, updateUiMethod):
        self.update_dock_widget_ui = updateUiMethod


    def cellPressed(self, x, y):
        liberties = np.zeros((self.board_size, self.board_size))
        self.info_label = ""

        # check if the move is valid
        if self.board_array[y][x] == 0:
            self.board_array[y][x] = 1 if self.white_turn else 2
        else:
            print("Move not valid")
            self.info_label = "Invalid move, the stone is already placed"
            return

        print(self.board_array)

        # get the liberties of each stone
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                liberties[i][j] = self.getLiberties(i, j)

        print(liberties)

        # get the stones that should be eaten
        eaten_stones = []

        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                if liberties[i][j] == 0:
                    if not self.board_array[i][j] == 0:
                        eaten_stones.append([i, j])
        print(eaten_stones)

        # check if the move is valid
        # if the placed stone has no liberties and no other stones are eaten, then exit
        if [y, x] in eaten_stones and len(eaten_stones) == 1:
            self.board_array[y][x] = 0
            print("Invalid move")
            self.info_label = "Illegal move"
            return

        # if the placed stone ate other stones, then continue
        # if the placed stone kills itself and a stone of the same color, then exit
        if [y, x] in eaten_stones:
            eaten_stones.remove([y, x])
            if self.board_array[y][x] in [self.board_array[s[0]][s[1]] for s in eaten_stones]:
                self.board_array[y][x] = 0
                print("Invalid move")
                self.info_label = "Illegal move"
                return
            else:
                liberties[y][x] = 1


        for state in self.states:
            if np.array_equal(state, self.board_array):
                print("Invalid move")
                self.board_array[y][x] = 0
                self.info_label = "Invalid move"
                return

        self.states = []
        self.states.append(self.board_array.copy())

        # update score, count eaten stones and delete them
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                if liberties[i][j] == 0:
                    if not self.board_array[i][j] == 0:
                        if self.white_turn:
                            self.white_score += 1
                            self.white_player_stones_eaten += 1
                        else:
                            self.black_score += 1
                            self.black_player_stones_eaten += 1
                    self.board_array[i][j] = 0
        print(self.white_player_stones_eaten)
        print(self.black_player_stones_eaten)
        self.update_dock_widget_ui()

        # count the territory
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                if not liberties[i][j] == self.prev_liberties[i][j] and liberties[i][j] == 0:
                    if self.white_turn:
                        self.white_score += 1
                        self.territory_controlled_by_white += 1
                    else:
                        self.black_score += 1
                        self.territory_controlled_by_black += 1

        print(f"Black player score: {self.black_score}")
        print(f"White player score: {self.white_score}")
        print(f"jfdhrh {self.territory_controlled_by_black}")
        print(f"oejfoe {self.territory_controlled_by_white}")
        if(self.buttonCount>0):
            self.buttonCount-=1
        print(self.buttonCount)
        self.update_dock_widget_ui()

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
        self.buttonCount+=1
        print(self.buttonCount)
        self.update_dock_widget_ui()


