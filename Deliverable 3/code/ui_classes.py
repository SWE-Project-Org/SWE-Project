from PyQt6.QtWidgets import QMainWindow, QWidget
from ui_py import main_menu_ui, find_route_ui, route_result_ui, select_route_ui


class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_menu_ui.Ui_MainWindow()  
        self.ui.setupUi(self) 
        self.ui.pushButton_2.clicked.connect(self.show_find_route_screen)
        self.show()

    def show_find_route_screen(self):
        self.deleteLater()
        self.find_route_window = FindRouteWindow()


class FindRouteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = find_route_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.show_select_route_screen)
        self.ui.pushButton_6.clicked.connect(self.show_main_menu_screen)
        self.show()

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu_window = MainMenuWindow()

    def show_select_route_screen(self):
        self.deleteLater()
        self.select_route_window = SelectRouteWindow()


class SelectRouteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = select_route_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.show_route_result_screen)
        self.ui.pushButton_3.clicked.connect(self.show_route_result_screen)
        self.ui.pushButton.clicked.connect(self.show_route_result_screen)
        self.ui.pushButton_8.clicked.connect(self.show_find_route_screen)
        self.show()

    def show_find_route_screen(self):
        self.deleteLater()
        self.find_route_window = FindRouteWindow()

    def show_route_result_screen(self):
        self.deleteLater()
        self.route_result_window = RouteResultWindow()


class RouteResultWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = route_result_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_8.clicked.connect(self.show_select_route_screen)
        self.ui.pushButton_9.clicked.connect(self.show_main_menu_screen)
        self.show()

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu_window = MainMenuWindow()

    def show_select_route_screen(self):
        self.deleteLater()
        self.select_route_window = SelectRouteWindow()    





