from PyQt6.QtWidgets import QWidget
from ui_py import scan_qr_ui
import main_menu

class RecentlyScannedScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = scan_qr_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_11.clicked.connect(self.show_main_menu_screen) #BACK
       # self.ui.pushButton_5.clicked.connect(self.placeholder) #

    def placeholder(self):
        pass

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()