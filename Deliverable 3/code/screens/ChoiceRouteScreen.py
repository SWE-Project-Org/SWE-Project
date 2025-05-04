import placeholder
from PyQt6.QtWidgets import QWidget
from ui_py import find_route_ui
import main_menu

class ChoiceRouteScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = find_route_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(placeholder) #
        self.ui.pushButton_6.clicked.connect(placeholder) #
        self.show()
