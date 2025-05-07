from PyQt6.QtWidgets import QWidget
from ui_py import food_info_ui

class FoodInformationScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = food_info_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_9.clicked.connect(self.show_recently_scanned) #DONE

    def show_recently_scanned(self):
        self.deleteLater()
        self.service.show_recently_scanned()
