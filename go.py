from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow,QLabel, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QPalette, QPixmap,QBrush
from board import Board
from constants import Constants
from dockWidget import DockWidget
from gameManager import GameManager
from PyQt5 import QtWidgets, QtGui


class Go(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # palette = QPalette()
        # palette.setBrush(QPalette.Background, QBrush(QPixmap('wood4k.jpg').scaled(self.size())))
        # self.setPalette(palette)
        # label = QLabel()
        # pixmap = QPixmap(".//school.jpg").scaled(self.size())
        # label.setPixmap(pixmap)
        # self.setCentralWidget(label)
        self.game_manager = GameManager(7)
        self.board = Board(self.game_manager)

        self.dock_widget = DockWidget(self.game_manager)
        self.game_manager.addUpdateUICallback(self.dock_widget.initUI)
        self.game_manager.addUpdateUIboard(self.board.update)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_widget)

        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.central_layout)
        # self.playerInfo = QWidget()
        # self.central_widget.setAutoFillBackground(True)
        # p = QPalette()
        # p.setColor(self.central_widget.backgroundRole(), Qt.GlobalColor.cyan)
        # p.setBrush(QPalette.Background, QBrush(QPixmap('woodTable.jpg')))
        # self.central_widget.setPalette(p)
        # self.setWidget(self.central_widget)
        self.central_widget.setStyleSheet("QWidget{background-color:#242924;}")
        # imagePath = ".//grey.jpg"
        # self.setStyleSheet(" QMainWindow{ background-image: url(" + imagePath + "); }")



        self.central_layout.addWidget(self.board)

        self.resize(Constants.WINDOW_SIZE)
        self.show()
