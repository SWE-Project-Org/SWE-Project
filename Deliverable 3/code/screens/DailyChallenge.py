from PyQt6.QtWidgets import QWidget
from ui_py import (daily_challenge_ui)

class DailyChallengeScreen(QWidget):
    def __init__(self,service):
        super().__init__()
        self.ui = daily_challenge_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
