from PyQt6.QtWidgets import QWidget
from ui_py import (activity_monitor_ui)

class ActivityMonitorScreen(QWidget):
    def __init__(self, service, activity):
        super().__init__()
        self.ui = activity_monitor_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_9.clicked.connect(self.service_end_activity)
        self.ui.label_5.setText(activity)
        self.ui.label_9.setText(str(0))
        self.ui.label_7.setText("00:00:00")
        

    def service_end_activity(self):
        self.deleteLater()
        self.service.end_activity()

    def update(self, heartrate, time, cal):
        self.ui.label_7.setText(time)
        self.ui.label_9.setText(cal)
        self.ui.label_11.setText(heartrate)
