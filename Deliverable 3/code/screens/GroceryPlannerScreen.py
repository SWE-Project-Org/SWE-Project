from PyQt6.QtWidgets import QWidget
from ui_py import (grocery_planner_ui)

def placeholder():
    pass

class CreateFoodPlanScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = grocery_planner_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.placeholder) #find groceries
    
    def placeholder(self):
        self.deleteLater()
        pass