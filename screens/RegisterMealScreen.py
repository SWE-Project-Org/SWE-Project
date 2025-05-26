from PyQt6.QtWidgets import QWidget
from ui_py import (register_meal_ui)
import main_menu


class RegisterMealScreen(QWidget):
    def __init__(self,service, food_list):
        super().__init__()
        self.ui = register_meal_ui.Ui_Form()
        self.service = service
        self.food_list = food_list
        self.ui.setupUi(self)
        self.ui.radioButton.setText(food_list[0][0]+" ("+str(food_list[0][1])+" kcal)")
        self.ui.radioButton_2.setText(food_list[1][0]+" ("+str(food_list[1][1])+" kcal)")
        self.ui.radioButton_3.setText(food_list[2][0]+" ("+str(food_list[2][1])+" kcal)")       
        self.ui.radioButton_4.setText(food_list[3][0]+" ("+str(food_list[3][1])+" kcal)")
        self.ui.label_4.setText("Calories consumed today:\n "+str(self.service.db.get_consumed_calories()))
        self.ui.pushButton_11.clicked.connect(self.show_main_menu_screen)
        self.ui.pushButton_5.clicked.connect(self.create_registered_meal_service) 


    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()    
    
    def create_registered_meal_service(self):
        self.deleteLater()
        if self.ui.radioButton.isChecked():
            self.service.create_registered_food(self.food_list[0][1])
        elif self.ui.radioButton_2.isChecked():
            self.service.create_registered_food(self.food_list[1][1])
        elif self.ui.radioButton_3.isChecked():
            self.service.create_registered_food(self.food_list[2][1])
        elif self.ui.radioButton_4.isChecked():
            self.service.create_registered_food(self.food_list[3][1])

    