from PyQt6.QtWidgets import QWidget
from ui_py import (daily_challenge_ui)

import main_menu


class DailyChallengeScreen(QWidget):
    def __init__(self, service, challenge=None, timer=None):
        super().__init__()
        self.ui = daily_challenge_ui.Ui_Form()
        self.service = service
        self.challenge = challenge
        self.timer = timer
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.reward_user) # done 
        self.ui.pushButton_6.clicked.connect(self.abort_challenge) # abort 
        self.ui.pushButton_11.clicked.connect(self.show_main_menu_screen) # back
        if self.challenge:
            self.set_challenge_data(self.challenge)
        if self.timer:
            self.timer.timeout.connect(self.update_timer_label)
            self.ui.label_timer.setText("00:00:00")

    def update_timer_label(self):
        if self.timer:
            time_str, _ = self.timer.time_elapsed()
            self.ui.label_timer.setText(time_str)

    def set_challenge_data(self, challenge):
        self.ui.label_4.setText(challenge.description)
        self.ui.label_6.setText(f"{challenge.calories} calories")
        self.ui.label_7.setText(f"This is a {challenge.difficulty} Challenge")

    # done button action
    def reward_user(self) -> None:
        if self.timer:
            self.timer.stop()
        self.deleteLater()
        self.service.challenge_completed()

    # abort button action
    def abort_challenge(self) -> None:
        if self.timer:
            self.timer.stop()
        self.deleteLater()
        self.service.challenge_aborted()

    def show_main_menu_screen(self):
        if self.timer:
            self.timer.stop()
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()

        