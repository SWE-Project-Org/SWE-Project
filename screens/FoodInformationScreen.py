from PyQt6.QtWidgets import QWidget
from ui_py import food_info_ui

class FoodInformationScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = food_info_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        # self.ui.label_7 is the food name label
        # self.ui.label_9 is the calories label
        # self.ui.label_11 is the vitamins label
        # self.ui.label_12 is the carbs label
        # self.ui.label_14 is the protein label
        # self.ui.label_16 is the fat label
        # self.ui.label_18 is the nutritional rating label
        # self.ui.label_20 is the price label
        self.ui.pushButton_9.clicked.connect(self.service_food_info_done) #DONE

    def service_food_info_done(self):
        self.deleteLater()
        self.service.food_info_done()
