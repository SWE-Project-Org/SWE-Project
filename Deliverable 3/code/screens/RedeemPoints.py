from PyQt6.QtWidgets import QWidget
from ui_py import (redeem_points_ui)


class RedeemPointsScreen(QWidget):
    def __init__(self,service):
        super().__init__()
        self.ui = redeem_points_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        # self.ui.pushButton_5.clicked.connect(placeholder) #My vouchers
        # self.ui.pushButton_6.clicked.connect(placeholder) #first coupon
        # self.ui.pushButton_7.clicked.connect(placeholder) #second
        # self.ui.pushButton_8.clicked.connect(placeholder) #third
        # self.ui.pushButton_9.clicked.connect(placeholder) #fourth
        # self.ui.pushButton_10.clicked.connect(placeholder) #fifth
        # self.ui.pushButton_11.clicked.connect(placeholder) #back
        # self.ui.pushButton_12.clicked.connect(placeholder) #redeem

