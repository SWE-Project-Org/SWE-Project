from PyQt6.QtWidgets import QWidget
from ui_py import (daily_challenge_ui)

import main_menu


class DailyChallengeScreen(QWidget):
    def __init__(self, service, challenge=None):
        super().__init__()
        self.ui = daily_challenge_ui.Ui_Form()
        self.service = service
        self.challenge = challenge
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.reward_user) # done 
        self.ui.pushButton_6.clicked.connect(self.abort_challenge) # abort 
        self.ui.pushButton_11.clicked.connect(self.show_main_menu_screen) # back
        if self.challenge:
            self.set_challenge_data(self.challenge)

    def set_challenge_data(self, challenge):
        self.ui.label_4.setText(challenge.description)
        self.ui.label_6.setText(f"{challenge.calories} calories")
        self.ui.label_7.setText(f"This is a {challenge.difficulty} Challenge")

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

        