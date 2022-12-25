from PyQt5.QtWidgets import QApplication
from go import Go
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myGo = Go()
    myGo.show()
    app.exec_()