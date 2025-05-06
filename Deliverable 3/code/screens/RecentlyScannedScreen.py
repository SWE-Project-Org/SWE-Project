from PyQt6.QtWidgets import QWidget
from ui_py import scan_qr_ui


class RecentlyScannedScreen(QWidget):
    def init(self):
        super().init()
        self.ui = scan_qr_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_11.clicked.connect(placeholder) #
        self.ui.pushButton_5.clicked.connect(placeholder) #