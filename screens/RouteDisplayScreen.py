from PyQt6.QtWidgets import QWidget
from ui_py import route_result_ui
import main_menu

class RouteDisplayScreen(QWidget):
    def __init__(self, service, selected_route):
        super().__init__()
        self.ui = route_result_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.label_4.setText(self.service.routes[selected_route].start + " - "
        + self.service.routes[selected_route].dest)
        self.ui.label_5.setText("Time: " + str(self.service.routes[selected_route].time) + "min")
        self.ui.label_6.setText("Calories: " + str(self.service.routes[selected_route].cal) + "kcal")
        self.ui.pushButton_8.clicked.connect(self.back_to_selection)
        self.ui.pushButton_9.clicked.connect(self.show_main_menu_screen) 

    def back_to_selection(self):
        self.deleteLater()
        self.service.returned_choice(None)

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()