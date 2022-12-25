from PyQt5.QtWidgets import QApplication,QStyleFactory,QToolBar,QComboBox,QFontDialog,QGridLayout,QDialog,QTextEdit, QWidget, QMainWindow, QFileDialog, QDockWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QPainter, QPen, QPixmap



class DockWidget(QDockWidget):
    """
    кароче чел класс гейм менеджер там альберт должен добавить всю хуйню которую тебе нужно будет выводить
    """
    def __init__(self, game_manager,board):
        super().__init__()
        self.board = board
        self.game_manager = game_manager
        self.playerInfo = QWidget()
        self.layout = QGridLayout()



        self.black_score= self.game_manager.black_score
        self.turnLabel = QLabel("")
        self.bolTurn = self.game_manager.white_turn
        self.initUI()

    def initUI(self):
        '''initiates ScoreBoard UI'''
        self.resize(200, 200)
        self.setFixedWidth(200)
        self.layout.setSpacing(2)
        self.layout.setRowStretch(7, 5)
        print("i" + str(self.black_score))
        self.setWindowTitle('ScoreBoard')
        self.playerInfo.setMaximumSize(100, self.height())
        self.layout.addWidget(QLabel("Scores:"), 1, 1)
        self.layout.addWidget(QLabel(str(self.black_score)), 2, 1)
        self.layout.addWidget(self.turnLabel, 3, 1)
        self.playerInfo.setLayout(self.layout)
        self.setWidget(self.playerInfo)
        print(self.bolTurn)

    def make_connection(self):
        '''this handles a signal sent from the board class'''
        # self.board.clickLocationSignal.connect(self.setClickLocation)
        # board.updateTimerSignal.connect(self.setTimeRemaining)
        # board.updatePrionersSignal.connect(self.updatePrisoners)
        # board.updateTerritoriesSignal.connect(self.updateTerritories)
        # board.showNotificationSignal.connect(self.displaynotification)
    def updateTurn(self):
        self.bolTurn = self.game_manager.white_turn
        if self.bolTurn:
            print("penis")
            self.turnLabel.setText("White player")
        else:
            print("kroll")
            self.turnLabel.setText("black player")


        # QApplication.processEvents()

        # self.game_manager.addUpdateUICallback(self)



