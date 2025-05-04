from PyQt6.QtWidgets import QWidget

# make this a popup 
class ConfirmScreen(QWidget):
    def __init__(self,service):
        super().__init__()
        # self.ui = daily_challenge_ui.Ui_Form() <-- make a confirm screen ui
        self.service = service
        # self.ui.setupUi(self)
