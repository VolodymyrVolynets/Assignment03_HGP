from PyQt5.QtWidgets import QApplication
from go import Go
import sys
if __name__ == '__main__':
    app = QApplication([])
    myGo = Go()
    sys.exit(app.exec_())