from PyQt5.QtWidgets import QWidget, QApplication, QFrame
from PyQt5.QtGui import QPainter, QMouseEvent, QColor
from PyQt5.QtCore import Qt
import sys, random

from constants import Constants


class Board(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setFixedSize(Constants.BOARD_SIZE)
        self.setStyleSheet("background-color:black;");
        self.board_size = 7
        print(self.getCellSize())
        self.intersection = [[]]
        for i in range(self.board_size):
            self.intersection.append([])
            for j in range(self.board_size):
                self.intersection[i].append([])
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.intersection[i][j] = [self.getCellSize() + int(self.getBoardSize() / (self.board_size - 1)) * i, self.getCellSize() + int(self.getBoardSize() / (self.board_size - 1)) * j]
        print(self.intersection)

    # def resizeEvent(self, *args, **kwargs):
    #     print(self.size())

    # def mousePressEvent(self, event: QMouseEvent):
    #     print(event)
    #     # painter = QtGui.QPainter(self.label.pixmap())
    #     # painter.drawLine(10, 10, 300, 200)
    #     # painter.end()
    #     # self.clicks.append(event.pos())
    #     # self.update()

    def paintEvent(self, e):
        qp = QPainter(self)
        self.drawBoard(qp)
        qp.end()

    def drawBoard(self, qp: QPainter):
        qp.setPen(QColor("white"))
        qp.drawRect(self.getCellSize(), self.getCellSize(), self.getBoardSize(), self.getBoardSize())
        for index in range(self.board_size - 1):
            # qp.drawLine(self.getBoardSize() / self.board_size * index, self.getCellSize(), self.getBoardSize() / self.board_size * index, self.getBoardSize() + self.getCellSize())
            x_offset = self.getCellSize()
            board_cell = int(self.getBoardSize() / (self.board_size - 1))
            qp.drawLine(x_offset + index * board_cell, self.getCellSize(), x_offset + index * board_cell, self.getBoardSize() + self.getCellSize())
            qp.drawLine(self.getCellSize(), x_offset + index * board_cell, self.getBoardSize() + self.getCellSize(), x_offset + index * board_cell)
        for i in self.intersection:
            for j in i:
                # print(self.intersection[i][j])
                qp.drawEllipse(j[0] - int(self.getCellSize() / 4), j[1] - int(self.getCellSize() / 4), int(self.getCellSize() / 2), int(self.getCellSize() / 2))
    def getCellSize(self):
        return int(self.size().width() / (self.board_size + 2))

    def getBoardSize(self):
        return int(self.getCellSize() * self.board_size)
