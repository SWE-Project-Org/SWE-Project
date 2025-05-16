from PyQt6.QtWidgets import QWidget
from ui_py import (register_meal_ui)

import main_menu


class RegisterMealScreen(QWidget):
    def __init__(self,service):
        super().__init__()
        self.ui = register_meal_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_11.clicked.connect(self.show_main_menu_screen)
        self.ui.pushButton_5.clicked.connect(self.show_main_menu_screen)  
 
    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()    
    
    def create_registered_meal_service(self):
        self.deleteLater()
        self.service.create_registered_food()

    