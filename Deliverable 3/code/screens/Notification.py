from PyQt6.QtWidgets import QWidget

# make this overay a small rect box in the upper right corner with the message 
class NotificationScreen(QWidget):
    def __init__(self,msg: str):
        super().__init__()
        # self.ui = daily_challenge_ui.Ui_Form() # notification screen ui
        # self.ui.setupUi(self)
        self.msg = msg

