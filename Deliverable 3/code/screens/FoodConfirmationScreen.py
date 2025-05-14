from PyQt6.QtWidgets import QWidget
from ui_py import confirm_food_ui
from services.FoodInformationService import FoodInformationService
from screens.Notification import NotificationScreen 
import main_menu


class FoodConfirmationScreen(QWidget):
    def __init__(self,service):
        super().__init__()
        self.ui = confirm_food_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_10.clicked.connect(self.show_notification_screen) #no
        self.ui.pushButton_9.clicked.connect(self.service_get_food_info) #yes

    def service_get_food_info(self):
        self.deleteLater()
        self.service.get_food_info()

    def show_notification_screen(self):
        self.deleteLater()
        self.notification_screen = NotificationScreen(self, "Challenge has been aborted")
        self.notification_screen.show()
        self.main_menu = main_menu.MainMenuScreen()