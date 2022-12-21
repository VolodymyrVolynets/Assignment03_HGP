from PyQt5.QtGui import QRegion
from PyQt5.QtWidgets import QPushButton
from PyQt5.uic.properties import QtGui

from constants import Constants


class Stone(QPushButton):
    def __init__(self,  label='', func=None, parent=None):
        super().__init__(parent)
        self.resize(Constants.STONE_SIZE)
        self.setMask(QRegion(self.rect(), QRegion.Ellipse))

    def setColor(self, color: str):
        self.setStyleSheet(
            f"background-color : {color};"
        )