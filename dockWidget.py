from PyQt5.QtWidgets import QApplication,QStyleFactory,QToolBar,QComboBox,QFontDialog,QGridLayout,QDialog,QTextEdit, QWidget, QMainWindow, QFileDialog, QDockWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QPainter, QPen, QPixmap



class DockWidget(QDockWidget):
    """
    кароче чел класс гейм менеджер там альберт должен добавить всю хуйню которую тебе нужно будет выводить
    """
    def __init__(self, game_manager):
        super().__init__()
        self.game_manager = game_manager
        self.playerInfo = QWidget()
        self.layout = QGridLayout()
        self.black_score= self.game_manager.black_score
        self.turnLabel = QLabel("")
        self.blackScoreLabel = QLabel("")
        self.bolTurn = self.game_manager.white_turn
        self.skipButton = QPushButton("Skip")
        self.skipButton.clicked.connect(self.updateSkipTurn)
        self.blackScoreText = QLabel("Black Score:")
        self.whiteScoreText = QLabel("White Score:")
        self.whiteScoreLabel = QLabel("")
        self.blackStonesEatenText = QLabel("White Stones Eaten:")
        self.whiteStonesEatenText = QLabel("Black Stones Eaten")
        self.blackStonesEatenLabel = QLabel("")
        self.whiteStonesEatenLabel = QLabel("")
        self.initUI()


    def initUI(self):
        '''initiates ScoreBoard UI'''
        self.resize(200, 400)
        self.setFixedWidth(200)
        self.setFixedSize(200,400)
        self.layout.setSpacing(2)
        print("i" + str(self.black_score))
        self.setWindowTitle('ScoreBoard')
        self.layout.addWidget(self.turnLabel, 1, 1)
        self.layout.addWidget(self.blackScoreText, 2, 1)
        self.layout.addWidget(self.blackScoreLabel,3,1)
        self.layout.addWidget(self.blackStonesEatenText,4,1)
        self.layout.addWidget(self.blackStonesEatenLabel,5,1)
        self.layout.addWidget(self.whiteScoreText,6,1)
        self.layout.addWidget(self.whiteScoreLabel,7,1)
        self.layout.addWidget(self.whiteStonesEatenText,8,1)
        self.layout.addWidget(self.whiteStonesEatenLabel,9,1)
        self.layout.addWidget(self.skipButton, 10, 1)
        self.playerInfo.setLayout(self.layout)
        self.setWidget(self.playerInfo)
        self.updateTurn()
        self.updateWhiteStones()
        self.updateBlackStones()
        self.updateBlackScore()
        self.updateWhiteScore()

    def updateTurn(self):
        self.bolTurn = self.game_manager.white_turn
        if self.bolTurn:
            self.turnLabel.setText("WHITE PLAYER TURN")
        else:
            self.turnLabel.setText("BLACK PLAYER TURN")

    def updateBlackScore(self):
        self.black_score = self.game_manager.black_score
        self.blackScoreLabel.setText(str(self.black_score))

    def updateSkipTurn(self):
        self.updateTurn()
        self.game_manager.passTurn()
        # QApplication.processEvents()
    def updateWhiteScore(self):
        self.whiteScoreLabel.setText(str(self.game_manager.white_score))

        # self.game_manager.addUpdateUICallback(self)
    def updateWhiteStones(self):
        self.whiteEaten = self.game_manager.white_player_stones_eaten
        print("white stones"+str(self.whiteEaten))
        self.whiteStonesEatenLabel.setText(str(self.whiteEaten))
    def updateBlackStones(self):
        self.blackEaten = self.game_manager.black_player_stones_eaten
        self.blackStonesEatenLabel.setText(str(self.blackEaten))



