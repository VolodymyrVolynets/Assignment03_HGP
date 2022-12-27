from PyQt5.QtWidgets import QGridLayout,QDialog, QWidget, QMainWindow, QFileDialog, QDockWidget, QPushButton, QLabel, QMessageBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QOpenGLTimerQuery, QPainter, QPen, QPixmap
from PyQt5.QtGui import QPalette, QPixmap,QBrush
from PyQt5.QtCore import QTimer


class DockWidget(QDockWidget):
    """
    кароче чел класс гейм менеджер там альберт должен добавить всю хуйню которую тебе нужно будет выводить
    """
    def __init__(self, game_manager):
        super().__init__()
        self.setStyleSheet("* {font-family: Areal; font-size: 16pt; font-weight: bold;color:white;}")
        # self.setStyleSheet("color: white;")
        self.game_manager = game_manager
        self.playerInfo = QWidget()
        self.timer = QTimer()
        self.timer.setInterval(1000)  # Set the interval to 1 second
        self.timer.timeout.connect(self.on_timeout)
        self.playerInfo.setStyleSheet("QWidget{background-color:#314532;}")
        self.layout = QVBoxLayout()
        self.black_score= self.game_manager.black_score
        self.turnLabel = QLabel("")
        self.blackScoreLabel = QLabel("")
        self.turn_label_text = QLabel("Turn:")
        self.bolTurn = self.game_manager.white_turn
        self.skipButton = QPushButton("Skip")
        self.skipButton.clicked.connect(self.updateSkipTurn)
        self.rulesButton = QPushButton("Rules")
        self.rulesButton.clicked.connect(self.goRulesDialog)
        self.skipButton.setStyleSheet("background-color:#6B8F45;")
        self.rulesButton.setStyleSheet("background-color:#6B8F45;")
        self.blackScoreText = QLabel("Score:")
        self.whiteScoreText = QLabel("Score:")
        self.whiteScoreLabel = QLabel("")
        self.blackStonesEatenText = QLabel("Stones:")
        self.whiteStonesEatenText = QLabel("Stones:")
        self.blackStonesEatenLabel = QLabel("")
        self.whiteStonesEatenLabel = QLabel("")
        self.error_message_label = QLabel("")
        self.error_message_label.setStyleSheet("color: red")
        self.whiteTerritoryText =QLabel("Territory:")
        self.blackTerritoryText = QLabel("Territory:")
        self.whiteTerritoryLabel = QLabel("")
        self.blackTerritoryLabel = QLabel("")
        self.restartButton = QPushButton("Restart")
        self.restartButton.clicked.connect(self.restartGame)
        self.restartButton.setStyleSheet("background-color:#6B8F45;")
        self.winLabel = QLabel("")

        turns_row = QHBoxLayout()
        turns_row.addWidget(self.turn_label_text)
        turns_row.addStretch(1)
        turns_row.addWidget(self.turnLabel)

        black_player_row = QHBoxLayout()
        black_player_row.addWidget(QLabel("Black player:"))

        black_score_row = QHBoxLayout()
        black_score_row.addWidget(self.blackScoreText)
        black_score_row.addStretch(1)
        black_score_row.addWidget(self.blackScoreLabel)

        white_player_row = QHBoxLayout()
        white_player_row.addWidget(QLabel("White player:"))

        white_score_row = QHBoxLayout()
        white_score_row.addWidget(self.whiteScoreText)
        white_score_row.addStretch(1)
        white_score_row.addWidget(self.whiteScoreLabel)

        black_stones_eaten_row = QHBoxLayout()
        black_stones_eaten_row.addWidget(self.blackStonesEatenText)
        black_stones_eaten_row.addStretch(1)
        black_stones_eaten_row.addWidget(self.blackStonesEatenLabel)

        white_stones_eaten = QHBoxLayout()
        white_stones_eaten.addWidget(self.whiteStonesEatenText)
        white_stones_eaten.addStretch(1)
        white_stones_eaten.addWidget(self.whiteStonesEatenLabel)

        black_territory_row = QHBoxLayout()
        black_territory_row.addWidget(self.blackTerritoryText)
        black_territory_row.addStretch(1)
        black_territory_row.addWidget(self.blackTerritoryLabel)

        white_territory_row = QHBoxLayout()
        white_territory_row.addWidget(self.whiteTerritoryText)
        white_territory_row.addStretch(1)
        white_territory_row.addWidget(self.whiteTerritoryLabel)

        win_row = QHBoxLayout()
        win_row.addWidget(self.winLabel)

        skip_button_row = QHBoxLayout()
        skip_button_row.addWidget(self.skipButton)

        error_row = QHBoxLayout()
        error_row.addWidget(self.error_message_label)

        restart_button_row = QHBoxLayout()
        restart_button_row.addWidget(self.restartButton)

        rules_button_row = QHBoxLayout()
        rules_button_row.addWidget(self.rulesButton)

        # self.layout.addWidget(QLabel("Turn:"), 1, 1)
        # self.layout.addWidget(self.turnLabel, 1, 2)
        # self.layout.addWidget(self.blackScoreText, 2, 1)
        # self.layout.addWidget(self.blackScoreLabel,2,2)
        # self.layout.addWidget(self.whiteScoreText,3,1)
        # self.layout.addWidget(self.whiteScoreLabel,3,2)
        # self.layout.addWidget(self.blackStonesEatenText,4,1)
        # self.layout.addWidget(self.blackStonesEatenLabel,5,1)
        # self.layout.addWidget(self.blackTerritoryText,6,1)
        # self.layout.addWidget(self.blackTerritoryLabel, 7, 1)
        # self.layout.addWidget(self.whiteStonesEatenText,10,1)
        # self.layout.addWidget(self.whiteStonesEatenLabel,11,1)
        # self.layout.addWidget(self.whiteTerritoryText,12,1 )
        # self.layout.addWidget(self.whiteTerritoryLabel,13,1 )
        # self.layout.addWidget(self.winLabel, 14, 1)
        # self.layout.addWidget(self.skipButton,14,1)
        # self.layout.addWidget(QLabel(""), 15, 1)
        # self.layout.addWidget(self.error_message_label,16,1)
        # self.layout.addWidget(QLabel(""), 17, 1)
        # self.layout.addWidget(self.restartButton, 18, 1)
        # self.layout.addWidget(QLabel(""), 19, 1)
        # self.layout.addWidget(self.rulesButton,20,1)
        # self.layout.addWidget(self.timer_display,21,1)

        self.layout.addLayout(turns_row)
        self.layout.addStretch(3)
        self.layout.addLayout(black_player_row)
        self.layout.addLayout(black_score_row)
        # self.layout.addStretch(1)
        self.layout.addLayout(black_stones_eaten_row)
        # self.layout.addStretch(1)
        self.layout.addLayout(black_territory_row)
        self.layout.addStretch(3)

        self.layout.addLayout(white_player_row)
        self.layout.addLayout(white_score_row)
        # self.layout.addStretch(3)
        self.layout.addLayout(white_stones_eaten)
        # self.layout.addStretch(3)
        self.layout.addLayout(white_territory_row)
        # self.layout.addStretch(3)
        self.layout.addLayout(win_row)

        self.layout.addStretch(30)
        self.layout.addLayout(error_row)
        self.layout.addLayout(skip_button_row)
        self.layout.addLayout(restart_button_row)
        self.layout.addLayout(rules_button_row)

        self.playerInfo.setLayout(self.layout)
        self.initUI()


    def initUI(self):
        '''initiates ScoreBoard UI'''
        # self.palette = QPalette()
        # self.palette.setBrush(QPalette.Background, QBrush(QPixmap('woodTable.jpg').scaled(self.size())))
        # self.setPalette(self.palette)
        self.counter = 120
        self.minutes = str(self.counter // 60)
        self.seconds = "0" + str(self.counter % 60) if self.counter % 60 < 10 else str(self.counter % 60)
        self.timer_display = QLabel(self.minutes + ":" + self.seconds)
        self.skipButton.show()
        self.winLabel.close()
        self.resize(250, 900)
        self.setFixedWidth(250)
        # self.setFixedSize(200,900)
        # self.layout.setSpacing(10)
        print("i" + str(self.black_score))
        # self.setWindowTitle('ScoreBoard')


        self.setWidget(self.playerInfo)
        self.updateErrorMessage()
        if(self.error_message_value==""):
            self.start_timer()
            self.updateTurn()
            self.updateWhiteStones()
            self.updateBlackStones()
            self.updateBlackScore()
            self.updateWhiteScore()
            self.updateWhiteTerritory()
            self.updateBlackTerritory()

    def start_timer(self):
        # Reset the counter to 120 (two minutes)

        # Start the timer
        self.timer.start()

    def on_timeout(self):
        # Decrement the counter by 1
        self.counter -= 1

        # Update the timer display
        self.minutes = str(self.counter // 60)
        self.seconds = "0" + str(self.counter % 60) if self.counter % 60 < 10 else str(self.counter % 60)
        self.timer_display.setText(self.minutes + ":" + self.seconds)

        # If the counter reaches 0, stop the timer and take the appropriate action
        if self.counter == 0:
            self.skipButton.close()
            if self.bolTurn:
                self.winLabel.setText("BLACK WINS")
            else:
                self.winLabel.setText("WHITE WINS")
            self.winLabel.show()
            self.timer.stop()

    def updateTurn(self):
        self.bolTurn = self.game_manager.white_turn
        if self.bolTurn:
            self.turnLabel.setText("White player")

        else:
            self.turnLabel.setText("Black player")

    def updateBlackScore(self):
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
        # QApplication.processEvents()
    def updateWhiteScore(self):
        self.whiteScoreLabel.setText(str(self.game_manager.white_score))

        # self.game_manager.addUpdateUICallback(self)
    def updateWhiteStones(self):
        self.whiteEaten = self.game_manager.white_player_stones_eaten
        self.whiteStonesEatenLabel.setText(str(self.whiteEaten))
    def updateBlackStones(self):
        self.blackEaten = self.game_manager.black_player_stones_eaten
        self.blackStonesEatenLabel.setText(str(self.blackEaten))
    def updateErrorMessage(self):
        self.error_message_value = self.game_manager.error_message
        self.timer.stop()
        self.error_message_label.setText(str(self.error_message_value))
    def updateBlackTerritory(self):
        self.blackTerritoryLabel.setText(str(self.game_manager.territory_controlled_by_black))

    def updateWhiteTerritory(self):
        self.whiteTerritoryLabel.setText(str(self.game_manager.territory_controlled_by_white))
    def goRulesDialog(self):
        self.dialogRules = QDialog()
        self.dialogRules.setStyleSheet("* {font-family: Areal; font-size: 16pt; font-weight: bold;color:white;background-color:#314532;}")
        self.rulesLayout = QGridLayout(self.dialogRules)
        self.rulesLabel = QLabel("A game of Go starts with an empty board.\n "
                                 "Each player has an effectively unlimited supply of pieces (called stones), one taking the black stones, the other taking white.\n"
                                 "The main object of the game is to use your stones to form territories by surrounding vacant areas of the board.\n "
                                 "It is also possible to capture your opponent's stones by completely surrounding them.\n"
                                 "Players take turns, placing one of their stones on a vacant point at each turn, with Black playing first.\n"
                                 "Note that stones are placed on the intersections of the lines rather than in the squares and once played stones are not moved.\n"
                                 "However they may be captured, in which case they are removed from the board, and kept by the capturing player as prisoners.")
        self.rulesLayout.addWidget(self.rulesLabel)
        self.dialogRules.show()
    def restartGame(self):
        self.game_manager.restartGame()





