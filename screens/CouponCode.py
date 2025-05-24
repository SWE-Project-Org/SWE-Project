from PyQt6.QtWidgets import QWidget
from models.CouponCode import CouponCode
from ui_py import my_vouchers_ui
import main_menu

class CouponCodeScreen(QWidget):
    def __init__(self,service,coupon_codes: list[CouponCode]):
        super().__init__()
        self.ui = my_vouchers_ui.Ui_Form()
        self.ui.setupUi(self)
        self.service = service
        self.coupon_codes = coupon_codes
        self.ui.pushButton_6.clicked.connect(self.show_main_menu_screen) #back button


    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()
