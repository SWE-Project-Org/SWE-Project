from PyQt6.QtWidgets import QWidget
from ui_py import (grocery_planner_ui)
from services.GroceryPlannerService import GroceryPlannerService

class CreateGroceryPlannerScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = grocery_planner_ui.Ui_Form()
        self.service = GroceryPlannerService()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.find_groceries) #find groceries
    
    def find_groceries(self):
        self.deleteLater()
        self.service.createGroceryService()

    def placeholder(self):
        self.deleteLater()
        pass