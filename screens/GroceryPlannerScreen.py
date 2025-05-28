from PyQt6.QtWidgets import QWidget
from ui_py import (grocery_planner_ui)
from services.GroceryPlannerService import GroceryPlannerService

class CreateGroceryPlannerScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = grocery_planner_ui.Ui_Form()
        self.service = service
        self.service = GroceryPlannerService(self.service.db, self.service.supermarket)
        self.ui.setupUi(self)
        # self.ui.lineEdit_2 is the desired budget input
        self.ui.pushButton_5.clicked.connect(self.find_groceries) #find groceries
    
    def find_groceries(self):
        try: 
            budget = float(self.ui.lineEdit_2.text())
        except ValueError:
            return
        self.deleteLater()
        self.service.createGroceryService(budget)

    def placeholder(self):
        self.deleteLater()
        pass