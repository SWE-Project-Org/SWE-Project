from PyQt6.QtWidgets import QWidget
from ui_py import my_vouchers_ui
import main_menu

class CouponCodeScreen(QWidget):
    def __init__(self,service):
        super().__init__()
        self.ui = my_vouchers_ui.Ui_Form()
        self.ui.setupUi(self)
        self.service = service
        self.ui.pushButton_6.clicked.connect(self.show_main_menu_screen) #back button


    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()
