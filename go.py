from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget

from board import Board
from constants import Constants
from stone import Stone


class Go(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.board = Board()
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.central_layout)


        self.central_layout.addWidget(self.board)

        self.resize(Constants.WINDOW_SIZE)
        self.show()
