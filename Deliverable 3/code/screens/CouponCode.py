from PyQt6.QtWidgets import QWidget

# make this a popup 
class CouponCodeScreen(QWidget):
    def __init__(self,service):
        super().__init__()
        # self.ui = daily_challenge_ui.Ui_Form() <-- make a couponCode screen ui
        self.service = service
        # self.ui.setupUi(self)