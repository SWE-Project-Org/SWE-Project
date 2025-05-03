from PyQt6.QtWidgets import QWidget
from ui_py import (select_activity_ui, activity_monitor_ui, activity_summary_ui)
import main_menu
  

class ActivitySelectionScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = select_activity_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_9.clicked.connect(self.service_create_activity)
        self.ui.pushButton_10.clicked.connect(self.service_create_activity)
        self.ui.pushButton_11.clicked.connect(self.show_main_menu_screen)

    def service_create_activity(self):
        self.deleteLater()
        self.service.create_activity()

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()


class ActivityMonitorScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = activity_monitor_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_9.clicked.connect(self.show_activity_summary_screen)
        
    def show_activity_summary_screen(self):
        self.deleteLater()
        self.service.end_activity()

    def update(self):
        pass


class ActivitySummaryScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = activity_summary_ui.Ui_Form()
        self.ui.setupUi(self)
        self.service = service
        self.ui.pushButton_9.clicked.connect(self.show_main_menu_screen)
        self.show()

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()

    
