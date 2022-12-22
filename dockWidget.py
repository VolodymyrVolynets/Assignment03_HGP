from PyQt5.QtWidgets import QDockWidget


class DockWidget(QDockWidget):
    """
    кароче чел класс гейм менеджер там альберт должен добавить всю хуйню которую тебе нужно будет выводить
    """
    def __init__(self, game_manager):
        super().__init__()
        self.game_manager = game_manager
        self.initUI()

    def initUI(self):
        '''initiates ScoreBoard UI'''
        self.resize(200, 200)
        self.setFixedWidth(200)
        # self.center()
        self.setWindowTitle('ScoreBoard')