from PyQt6.QtWidgets import QWidget
from ui_py import (redeem_points_ui)


class RedeemPointsScreen(QWidget):
    def __init__(self,service):
        super().__init__()
        self.ui = redeem_points_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)


