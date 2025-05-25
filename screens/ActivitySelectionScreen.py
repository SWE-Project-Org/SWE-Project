from PyQt6.QtWidgets import QWidget
from ui_py import select_activity_ui
import main_menu
  
class ActivitySelectionScreen(QWidget):
    def __init__(self, service, activities):
        super().__init__()
        self.ui = select_activity_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.activities = activities
        self.ui.pushButton_9.setText(activities[0][1])
        self.ui.pushButton_10.setText(activities[1][1])
        self.ui.pushButton_9.clicked.connect(self.service_create_activity1)
        self.ui.pushButton_10.clicked.connect(self.service_create_activity2)
        self.ui.pushButton_11.clicked.connect(self.show_main_menu_screen)

    def service_create_activity1(self):
        self.deleteLater()
        self.service.create_activity(self.activities[0][1], self.activities[0][2])

    def service_create_activity2(self):
        self.deleteLater()
        self.service.create_activity(self.activities[1][1], self.activities[1][2])

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()