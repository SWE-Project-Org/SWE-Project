from PyQt6.QtWidgets import QWidget
from ui_py import (daily_challenge_ui)

import main_menu


class DailyChallengeScreen(QWidget):
    def __init__(self,service):
        super().__init__()
        self.ui = daily_challenge_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.reward_user) # done 
        self.ui.pushButton_6.clicked.connect(self.abort_challenge) # abort 
        self.ui.pushButton_11.clicked.connect(self.show_main_menu_screen) # back

    # done button action
    def reward_user(self) -> None:
        self.deleteLater()
        self.service.challenge_completed()

    # abort button action
    def abort_challenge(self) -> None:
        self.deleteLater()
        self.service.challenge_aborted()

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()
