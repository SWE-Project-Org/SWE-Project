from PyQt6.QtWidgets import QMainWindow
import services.RewardService
from ui_py import (main_menu_ui)
from service_classes import ActivityMonitorService
from services.ChallengeService import ChallengeService
from services.ImageUploadService import ImageUploadService
import services
from support_classes import DBManager

class MainMenuScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_menu_ui.Ui_MainWindow()  
        self.ui.setupUi(self) 
        self.ui.pushButton_8.clicked.connect(self.monitor_activity_service)
        self.ui.pushButton_7.clicked.connect(self.challenge_service)
        self.ui.pushButton_6.clicked.connect(self.image_upload_service)
        self.show()

    def monitor_activity_service(self):
        self.deleteLater()
        monitor_activity_obj = ActivityMonitorService()
        monitor_activity_obj.monitor_activity()

    def challenge_service(self):
        self.deleteLater()
        db = DBManager()
        challenge_service = ChallengeService(db,services.RewardService.RewardService(db))
        challenge_service.start_daily_challenge()

    def image_upload_service(self):
        self.deleteLater()
        image_upload_service = ImageUploadService()
        image_upload_service.show_food_confirmation()
