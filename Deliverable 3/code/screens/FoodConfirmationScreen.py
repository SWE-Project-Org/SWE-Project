from PyQt6.QtWidgets import QWidget
from ui_py import confirm_food_ui
from services.FoodInformationService import FoodInformationService


class FoodConfirmationScreen(QWidget):
    def __init__(self,service):
        super().__init__()
        self.ui = confirm_food_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_10.clicked.connect(self.placeholder)
        self.ui.pushButton_9.clicked.connect(self.service_get_food_info) #yes

    def placeholder(self):
        pass

    def service_get_food_info(self):
        self.deleteLater()
        service_get_food_info = FoodInformationService()
        service_get_food_info.get_food_info()
