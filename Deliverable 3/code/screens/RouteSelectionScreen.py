import placeholder
from PyQt6.QtWidgets import QWidget
from ui_py import select_route_ui
import main_menu

class RouteSelectionScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = select_route_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(placeholder) #
        self.ui.pushButton_3.clicked.connect(placeholder) #
        self.ui.pushButton.clicked.connect(placeholder) #
        self.ui.pushButton_8.clicked.connect(placeholder) #
