from PyQt6.QtWidgets import QWidget
from ui_py import find_route_ui
import main_menu

class ChoiceEntryScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = find_route_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.return_choices_service)
        self.ui.pushButton_6.clicked.connect(self.show_main_menu_screen) 

    
    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()

    def return_choices_service(self):
        self.deleteLater()
        self.activity = self.ui.comboBox.currentText()
        self.start = self.ui.lineEdit_2.text()
        self.cal = int(self.ui.lineEdit.text())
        self.service.returned_choice([self.activity, self.start, self.cal])

    
