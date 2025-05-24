from PyQt6.QtWidgets import QWidget
from ui_py import confirm_food_ui

# make this a popup 
class ConfirmScreen(QWidget):
    def __init__(self,service):
        super().__init__()
        # self.ui = confirm_food_ui.Ui_Form() 
        self.service = service
        # self.ui.setupUi(self)
