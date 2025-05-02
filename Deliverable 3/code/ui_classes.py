# This Python file uses the following encoding: utf-8
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from ui_py import main_menu_ui, find_route_ui, route_result_ui, select_route_ui

class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_menu_ui.Ui_MainWindow()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Setup the UI in the main window
        self.find_route_window = FindRouteWindow()
        self.ui.pushButton_2.clicked.connect(self.show_find_route_screen)
        self.show()

    def show_find_route_screen(self):
        self.hide()
        self.find_route_window.show()

class FindRouteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = find_route_ui.Ui_Form()
        self.select_route_window = SelectRouteWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.show_select_route_screen)

    def show_select_route_screen(self):
        self.hide()
        self.select_route_window.show()

class SelectRouteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = select_route_ui.Ui_Form()
        self.route_result_window = RouteResultWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.show_route_result_screen)
        self.ui.pushButton_3.clicked.connect(self.show_route_result_screen)
        self.ui.pushButton.clicked.connect(self.show_route_result_screen)

    def show_route_result_screen(self):
        self.hide()
        self.route_result_window.show()

class RouteResultWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = route_result_ui.Ui_Form()
        self.ui.setupUi(self)





