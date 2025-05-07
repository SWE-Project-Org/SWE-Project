from PyQt6.QtWidgets import QWidget
from ui_py import confirm_food_ui

class FoodConfirmationScreen(QWidget):
    def init(self):
        super().init()
        self.ui = confirm_food_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_10.clicked.connect(placeholder) #
        self.ui.pushButton_9.clicked.connect(placeholder) #