import placeholder
from PyQt6.QtWidgets import QWidget
from ui_py import route_result_ui

class RouteDisplayScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = route_result_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_8.clicked.connect(placeholder) #
        self.ui.pushButton_9.clicked.connect(placeholder) #