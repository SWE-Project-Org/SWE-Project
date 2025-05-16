from PyQt6.QtWidgets import QWidget
from ui_py import route_result_ui
import main_menu

class RouteDisplayScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = route_result_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_8.clicked.connect(self.back_to_selection)
        self.ui.pushButton_9.clicked.connect(self.show_main_menu_screen) 

    def back_to_selection(self):
        self.deleteLater()
        self.service.returned_choice('running')

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()