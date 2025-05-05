from PyQt6.QtWidgets import QWidget
from ui_py import (food_plan_summary_ui)
import main_menu

def placeholder():
    pass

class FoodPlanSummaryScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = food_plan_summary_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_9.clicked.connect(self.placeholder) #export to pdf
        self.ui.pushButton_10.clicked.connect(self.show_main_menu_screen) #main menu



    def placeholder(self):
        self.deleteLater()
        pass

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()
