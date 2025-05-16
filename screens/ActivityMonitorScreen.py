from PyQt6.QtWidgets import QWidget
from ui_py import (activity_monitor_ui)

class ActivityMonitorScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = activity_monitor_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_9.clicked.connect(self.service_end_activity)
        
    def service_end_activity(self):
        self.deleteLater()
        self.service.end_activity()

    def update(self):
        pass