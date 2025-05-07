from PyQt6.QtWidgets import QWidget
from ui_py import confirm_food_ui

class FoodConfirmationScreen(QWidget):
    def __init__(self,service):
        super().__init__()
        self.ui = confirm_food_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_10.clicked.connect(self.placeholder) #
        self.ui.pushButton_9.clicked.connect(self.placeholder) #

    def placeholder(self):
        pass