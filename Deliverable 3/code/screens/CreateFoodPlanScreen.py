from PyQt6.QtWidgets import QWidget
from ui_py import (create_food_plan_ui)



class CreateFoodPlanScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = create_food_plan_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_6.clicked.connect(self.placeholder) #back to main menu
        self.ui.pushButton_5.clicked.connect(self.placeholder) #go to grocery planner

    def placeholder(self):
        self.deleteLater()
        pass