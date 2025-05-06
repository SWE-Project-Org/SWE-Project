from PyQt6.QtWidgets import QWidget
from ui_py import food_info_ui

class FoodInformationScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = food_info_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_9.clicked.connect(placeholder) #