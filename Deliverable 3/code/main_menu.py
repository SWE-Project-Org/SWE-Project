from PyQt6.QtWidgets import QMainWindow
import services.RewardService
from ui_py import (main_menu_ui)
from service_classes import ActivityMonitorService
from services.ChallengeService import ChallengeService
from services.RewardService import RewardService
from services.RegisterMealService import RegisterMealService
from models.Supermarket import Supermarket
import services
from support_classes import DBManager

class MainMenuScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_menu_ui.Ui_MainWindow()  
        self.ui.setupUi(self) 
        self.ui.pushButton_8.clicked.connect(self.monitor_activity_service)
        self.ui.pushButton_7.clicked.connect(self.reward_service)
        self.ui.pushButton.clicked.connect(self.challenge_service)
        self.ui.pushButton_3.clicked.connect(self.register_meal_service)
        self.show()

    def register_meal_service(self):
        self.deleteLater()
        db = DBManager()
        supermarket = Supermarket()
        self.register_meal_obj = RegisterMealService(db, supermarket)
        self.register_meal_obj.register_food()

    def monitor_activity_service(self):
        self.deleteLater()
        monitor_activity_obj = ActivityMonitorService()
        monitor_activity_obj.monitor_activity()

    def challenge_service(self):
        self.deleteLater()
        db = DBManager()
        challenge_service = ChallengeService(db,services.RewardService.RewardService(db))
        challenge_service.start_daily_challenge()

    def reward_service(self):
        self.deleteLater()
        db = DBManager()
        reward_service = RewardService(db)
        reward_service.get_offers()