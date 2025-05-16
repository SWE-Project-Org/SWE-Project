from PyQt6.QtWidgets import QWidget
from ui_py import notification_ui
from PyQt6.QtCore import QTimer

class NotificationScreen(QWidget):
    def __init__(self,msg: str, service):
        super().__init__()
        self.ui = notification_ui.Ui_Form()
        self.ui.setupUi(self)
        self.service = service
        self.msg = msg
        self.show()
        QTimer.singleShot(3000, self.close)

