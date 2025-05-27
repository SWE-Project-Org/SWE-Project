from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from models.CouponCode import CouponCode
from ui_py import my_vouchers_ui
import main_menu

class CouponCodeScreen(QWidget):
    def __init__(self,service,coupon_codes: list):
        super().__init__()
        self.ui = my_vouchers_ui.Ui_Form()
        self.ui.setupUi(self)
        self.service = service
        self.coupon_codes = coupon_codes
        self.ui.pushButton_6.clicked.connect(self.show_main_menu_screen) #back button

        # List of hardcoded label names in order
        label_names = [f'label_{i}' for i in range(6, 13)]  # label_6 to label_12
        labels = [getattr(self.ui, name) for name in label_names if hasattr(self.ui, name)]

        # Fill labels with coupon codes
        for i, label in enumerate(labels):
            if i < len(self.coupon_codes):
                code, description, validTill = self.coupon_codes[i]
                label.setText(f"{description}, {code}")
                label.show()
            else:
                label.setText("")
                label.hide()

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()
