from PyQt6.QtWidgets import QWidget
from ui_py import (weekly_progress_ui)

import main_menu


class WeeklyProgressScreen(QWidget):
    def __init__(self,service):
        super().__init__()
        self.ui = weekly_progress_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_11.clicked.connect(self.show_main_menu_screen)
        self.ui.pushButton_9.clicked.connect(self.export_to_pdf_service)  
 
    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()    
    
    def export_to_pdf_service(self):
        self.service.export()