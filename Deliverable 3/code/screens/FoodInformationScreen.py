from PyQt6.QtWidgets import QWidget
from ui_py import food_info_ui

class FoodInformationScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = food_info_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_9.clicked.connect(self.service_food_info_done) #DONE

    def service_food_info_done(self):
        self.deleteLater()
        self.service.food_info_done()
