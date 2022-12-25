from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget

from board import Board
from constants import Constants
from dockWidget import DockWidget
from gameManager import GameManager


class Go(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.game_manager = GameManager(7)
        self.board = Board(self.game_manager)

        self.dock_widget = DockWidget(self.game_manager,self.board)
        # self.game_manager.addUpdateUICallback(self.dock_widget.update)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_widget)

        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.central_layout)


        self.central_layout.addWidget(self.board)

        self.resize(Constants.WINDOW_SIZE)
        self.show()
