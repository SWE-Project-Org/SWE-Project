from PyQt6.QtWidgets import QMainWindow
from ui_py import (main_menu_ui)
from service_classes import ActivityMonitorService

class MainMenuScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_menu_ui.Ui_MainWindow()  
        self.ui.setupUi(self) 
        self.ui.pushButton_8.clicked.connect(self.monitor_activity_service)
        self.show()
    
    def monitor_activity_service(self):
        self.deleteLater()
        monitor_activity_obj = ActivityMonitorService()
        monitor_activity_obj.monitor_activity()