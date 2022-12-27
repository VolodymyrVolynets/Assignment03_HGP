from math import sqrt

from PyQt5.QtWidgets import QWidget,QLabel ,QApplication, QFrame
from PyQt5.QtGui import QPainter, QMouseEvent, QColor
from PyQt5.QtGui import QPalette,QGradient, QPixmap,QBrush
from PyQt5.QtCore import Qt,QRectF,QRect
import sys, random

from constants import Constants
from gameManager import GameManager


class Board(QFrame):
    def __init__(self, game_manager: GameManager, parent=None):
        super().__init__(parent)
        self.game_manager = game_manager
        self.initUI()

    def initUI(self):
        self.setFixedSize(Constants.BOARD_SIZE)
        # self.palette = QPalette()
        # self.palette.setBrush(QPalette.Background, QBrush(QPixmap('grey.jpg').scaled(self.size())))
        # self.setPalette(self.palette)
        #
        # label = QLabel()
        # pixmap = QPixmap(".//school.jpg").scaled(self.size())
        # label.setPixmap(pixmap)
        # self.setCentralWidget(label)

        # self.setStyleSheet("QFrame{background-color:#5DC470;}")
        # self.setStyleSheet("QFrame { background-image: url(" + imagePath + "); }")
        self.board_size = 7
        print(self.getCellSize())
        self.intersection = [[]]
        for i in range(self.board_size):
            self.intersection.append([])
            for j in range(self.board_size):
                self.intersection[i].append([])
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.intersection[i][j] = [self.getCellSize() + self.getCellSize() * i, self.getCellSize() + self.getCellSize() * j]

        # self.game_manager.cellPressed(0, 0)

    # def resizeEvent(self, *args, **kwargs):
    #     print(self.size())

    def mousePressEvent(self, event: QMouseEvent):
        click_x = event.pos().x()
        click_y = event.pos().y()
        nearest_index = []


        for i in range(len(self.intersection)):
            for j in range(len(self.intersection[i])):
                distance = sqrt((click_x - self.intersection[i][j][0])**2 + (click_y - self.intersection[i][j][1])**2)
                if distance <= self.getCellSize() / 4:
                    nearest_index.append(i)
                    nearest_index.append(j)
                    break
        if nearest_index:
            self.cellPressed(nearest_index[0], nearest_index[1])

    def addUpdateUICallback(self, updateUiMethod):
        self.update_dock_widget_ui = updateUiMethod

    def cellPressed(self, x, y):
        self.game_manager.cellPressed(x, y)
        self.update()

    def paintEvent(self, e):
        qp = QPainter(self)
        self.drawBoard(qp)
        self.drawCircles(qp)
        qp.end()

    def drawCircles(self, qp: QPainter):
        for i in range(self.game_manager.board_size):
            for j in range(self.game_manager.board_size):
                if self.game_manager.board_array[i][j] != 0:
                    if self.game_manager.board_array[i][j] == 1:
                        qp.setBrush(QColor("white"))
                    elif self.game_manager.board_array[i][j] == 2:
                        qp.setBrush(QColor("black"))
                    qp.drawEllipse(self.intersection[i][j][1] - int(self.getCellSize() / 4), self.intersection[i][j][0] - int(self.getCellSize() / 4), int(self.getCellSize() / 2), int(self.getCellSize() / 2))

    def drawBoard(self, qp: QPainter):
        qp.setPen(QColor("white"))
        for index in range(self.board_size):
            qp.drawLine(
                self.getCellSize() + index * self.getCellSize(),
                self.getCellSize(),
                self.getCellSize() + index * self.getCellSize(),
                self.getCellSize() + self.getCellSize() * (self.board_size - 1)
            )
            qp.drawLine(
                self.getCellSize(),
                self.getCellSize() + index * self.getCellSize(),
                self.getCellSize() + self.getCellSize() * (self.board_size - 1),
                self.getCellSize() + index * self.getCellSize()
                )
            # Set the brush color to a color of your choice
            qp.setBrush(QColor("red"))

            # Calculate the size of each cell
            cell_size = self.getCellSize()

            # Loop through all the rows and columns of the board
            for row in range(self.board_size-1):
                for col in range(self.board_size-1):
                    # Calculate the x and y coordinates of the top left corner of the cell
                    x = self.getCellSize() + col * cell_size
                    y = self.getCellSize() + row * cell_size

                    # Use the fillRect method to draw a filled rectangle at the calculated coordinates
                    rect = QRectF(x, y, cell_size, cell_size)
                    if (row + col) % 2 == 0:
                        qp.setBrush(QColor("#6B8F45"))
                    else:
                        qp.setBrush(QColor("#DFC8A8"))
                    qp.fillRect(rect, qp.brush())
    def getCellSize(self):
        return int(self.size().width() / (self.board_size + 1))

    # def getBoardSize(self):
    #     return int(self.getCellSize() * self.board_size)
