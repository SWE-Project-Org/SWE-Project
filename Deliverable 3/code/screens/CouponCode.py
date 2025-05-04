from PyQt6.QtWidgets import QWidget

# make this a popup 
class CouponCodeScreen(QWidget):
    def __init__(self,service):
        self.service = service