from PyQt6.QtWidgets import QWidget
from ui_py import my_vouchers_ui

class CouponCodeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = my_vouchers_ui.Ui_Form()
        self.ui.setupUi(self)
        # self.ui.pushButton_6.clicked.connect(placeholder) #back button