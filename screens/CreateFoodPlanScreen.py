from PyQt6.QtWidgets import QWidget
from ui_py import (create_food_plan_ui)
import main_menu
from services.GroceryPlannerService import GroceryPlannerService



class CreateFoodPlanScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = create_food_plan_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        # self.ui.comboBox is the goal dropdown
        # self.ui.lineEdit_2 is the desired weight input
        self.ui.pushButton_6.clicked.connect(self.show_main_menu_screen) #back to main menu
        self.ui.pushButton_5.clicked.connect(self.go_to_grocery_planner) #go to grocery planner

    def go_to_grocery_planner(self):
        self.deleteLater()
        self.service.enterGoal()

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()

    def placeholder(self):
        self.deleteLater()
        pass