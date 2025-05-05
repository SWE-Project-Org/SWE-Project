from PyQt6.QtWidgets import QWidget
from ui_py import daily_challenge_ui,my_vouchers_ui, redeem_points_ui

class DailyChallengeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = daily_challenge_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(placeholder) #
        self.ui.pushButton_6.clicked.connect(placeholder) #
        self.ui.pushButton_11.clicked.connect(placeholder) #
    
    def placeholder():
        servi

class RedeemPointsScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = redeem_points_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(placeholder) #My vouchers
        self.ui.pushButton_6.clicked.connect(placeholder) #first coupon
        self.ui.pushButton_7.clicked.connect(placeholder) #second
        self.ui.pushButton_8.clicked.connect(placeholder) #third
        self.ui.pushButton_9.clicked.connect(placeholder) #fourth
        self.ui.pushButton_10.clicked.connect(placeholder) #fifth
        self.ui.pushButton_11.clicked.connect(placeholder) #back
        self.ui.pushButton_12.clicked.connect(placeholder) #redeem


class CouponCodeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = my_vouchers_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_6.clicked.connect(placeholder) #back button

