from PyQt5.QtWidgets import QStyleFactory,QToolBar,QComboBox,QFontDialog,QGridLayout,QDialog,QTextEdit, QWidget, QMainWindow, QFileDialog, QDockWidget, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QPainter, QPen, QPixmap
from PyQt5.QtGui import QPalette, QPixmap,QBrush


class DockWidget(QDockWidget):
    """
    кароче чел класс гейм менеджер там альберт должен добавить всю хуйню которую тебе нужно будет выводить
    """
    def __init__(self, game_manager):
        super().__init__()
        self.game_manager = game_manager
        self.playerInfo = QWidget()
        self.playerInfo.setStyleSheet("QWidget{background-color:#5DC470;}")
        self.layout = QGridLayout()
        self.black_score= self.game_manager.black_score
        self.turnLabel = QLabel("")
        self.blackScoreLabel = QLabel("")
        self.bolTurn = self.game_manager.white_turn
        self.skipButton = QPushButton("Skip")
        self.skipButton.clicked.connect(self.updateSkipTurn)
        self.rulesButton = QPushButton("Rules")
        self.rulesButton.clicked.connect(self.goRulesDialog)
        self.skipButton.setStyleSheet("background-color:green;")
        self.rulesButton.setStyleSheet("background-color:green;")
        self.blackScoreText = QLabel("Black Score:")
        self.whiteScoreText = QLabel("White Score:")
        self.whiteScoreLabel = QLabel("")
        self.blackStonesEatenText = QLabel("White Stones Eaten:")
        self.whiteStonesEatenText = QLabel("Black Stones Eaten")
        self.blackStonesEatenLabel = QLabel("")
        self.whiteStonesEatenLabel = QLabel("")
        self.error_message_label = QLabel("")
        self.whiteTerritoryText =QLabel("White Territory:")
        self.blackTerritoryText = QLabel("Black Territory:")
        self.whiteTerritoryLabel = QLabel("")
        self.blackTerritoryLabel = QLabel("")
        self.restartButton = QPushButton("Restart")
        self.restartButton.clicked.connect(self.restartGame)
        self.restartButton.setStyleSheet("background-color:green;")
        self.winLabel = QLabel("")
        self.initUI()


    def initUI(self):
        '''initiates ScoreBoard UI'''
        # self.palette = QPalette()
        # self.palette.setBrush(QPalette.Background, QBrush(QPixmap('woodTable.jpg').scaled(self.size())))
        # self.setPalette(self.palette)
        self.skipButton.show()
        self.winLabel.close()
        self.resize(200, 900)
        self.setFixedWidth(200)
        # self.setFixedSize(200,900)
        self.layout.setSpacing(10)
        print("i" + str(self.black_score))
        self.setWindowTitle('ScoreBoard')
        self.layout.addWidget(self.turnLabel, 1, 1)
        self.layout.addWidget(self.blackScoreText, 2, 1)
        self.layout.addWidget(self.blackScoreLabel,3,1)
        self.layout.addWidget(self.blackStonesEatenText,4,1)
        self.layout.addWidget(self.blackStonesEatenLabel,5,1)
        self.layout.addWidget(self.blackTerritoryText,6,1)
        self.layout.addWidget(self.blackTerritoryLabel, 7, 1)
        self.layout.addWidget(self.whiteScoreText,8,1)
        self.layout.addWidget(self.whiteScoreLabel,9,1)
        self.layout.addWidget(self.whiteStonesEatenText,10,1)
        self.layout.addWidget(self.whiteStonesEatenLabel,11,1)
        self.layout.addWidget(self.whiteTerritoryText,12,1 )
        self.layout.addWidget(self.whiteTerritoryLabel,13,1 )
        self.layout.addWidget(self.winLabel, 14, 1)
        self.layout.addWidget(self.skipButton,14,1)
        self.layout.addWidget(QLabel(""), 15, 1)
        self.layout.addWidget(self.error_message_label,16,1)
        self.layout.addWidget(QLabel(""), 17, 1)
        self.layout.addWidget(self.restartButton, 18, 1)
        self.layout.addWidget(QLabel(""), 19, 1)
        self.layout.addWidget(self.rulesButton,20,1)
        self.playerInfo.setLayout(self.layout)
        self.setWidget(self.playerInfo)
        self.updateErrorMessage()
        if(self.error_message_value==""):
            self.updateTurn()
            self.updateWhiteStones()
            self.updateBlackStones()
            self.updateBlackScore()
            self.updateWhiteScore()
            self.updateWhiteTerritory()
            self.updateBlackTerritory()
    def updateTurn(self):
        self.bolTurn = self.game_manager.white_turn
        print(self.bolTurn)
        if not self.bolTurn:
            self.turnLabel.setText("WHITE PLAYER TURN")

        else:
            self.turnLabel.setText("BLACK PLAYER TURN")

    def updateBlackScore(self):
        print("PISOS")
        self.black_score = self.game_manager.black_score
        self.blackScoreLabel.setText(str(self.black_score))

    def updateSkipTurn(self):
        self.game_manager.passTurn()
        self.updateTurn()
        if(self.game_manager.buttonCount>=2):
            self.skipButton.close()
            if(self.game_manager.black_score>self.game_manager.white_score):
                self.winLabel.setText("BLACK WINS")
            elif (self.game_manager.black_score == self.game_manager.white_score):
                self.winLabel.setText("EVEN")
            elif (self.game_manager.black_score < self.game_manager.white_score):
                self.winLabel.setText("WHITE WINS")
            self.winLabel.show()
            print("2 times skiped")
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
    def updateErrorMessage(self):
        self.error_message_value = self.game_manager.error_message
        print("error"+str(self.error_message_value))
        self.error_message_label.setText(str(self.error_message_value))
    def updateBlackTerritory(self):
        self.blackTerritoryLabel.setText(str(self.game_manager.territory_controlled_by_black))

    def updateWhiteTerritory(self):
        self.whiteTerritoryLabel.setText(str(self.game_manager.territory_controlled_by_white))
    def goRulesDialog(self):
        self.dialogRules = QDialog()
        self.rulesLayout = QGridLayout(self.dialogRules)
        self.rulesLabel = QLabel("A game of Go starts with an empty board.\n "
                                 "Each player has an effectively unlimited supply of pieces (called stones), one taking the black stones, the other taking white.\n"
                                 "The main object of the game is to use your stones to form territories by surrounding vacant areas of the board.\n "
                                 "It is also possible to capture your opponent's stones by completely surrounding them.Players take turns, placing one of their stones on a vacant point at each turn, with Black playing first.\n"
                                 "Note that stones are placed on the intersections of the lines rather than in the squares and once played stones are not moved.\n"
                                 "However they may be captured, in which case they are removed from the board, and kept by the capturing player as prisoners.")
        self.rulesLayout.addWidget(self.rulesLabel)
        self.dialogRules.show()
    def restartGame(self):
        self.game_manager.restartGame()





