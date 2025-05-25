from PyQt6.QtWidgets import QWidget
from ui_py import activity_summary_ui
import main_menu
  
class ActivitySummaryScreen(QWidget):
    def __init__(self, service, activity, time, cal):
        super().__init__()
        self.ui = activity_summary_ui.Ui_Form()
        self.ui.setupUi(self)
        self.service = service
        self.ui.label_5.setText(activity)
        self.ui.label_7.setText(time)
        self.ui.label_9.setText(cal)
        self.ui.pushButton_9.clicked.connect(self.show_main_menu_screen)

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()