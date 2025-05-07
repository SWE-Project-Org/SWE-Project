from PyQt6.QtWidgets import QWidget
from ui_py import select_activity_ui
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