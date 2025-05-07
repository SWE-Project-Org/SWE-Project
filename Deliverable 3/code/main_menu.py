from PyQt6.QtWidgets import QMainWindow
import services.RewardService
from ui_py import (main_menu_ui)
from services.ChallengeService import ChallengeService
from services.RewardService import RewardService
from services.RegisterMealService import RegisterMealService
from services.WeeklyProgressService import WeeklyProgressService
from models.Supermarket import Supermarket
from services.MapService import MapService
from services.ActivityMonitorService import ActivityMonitorService
from services.FoodPlannerService import FoodPlannerService
import services
from support_classes import DBManager, SmartWatch





class MainMenuScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_menu_ui.Ui_MainWindow()  
        self.ui.setupUi(self) 
        self.ui.pushButton_8.clicked.connect(self.monitor_activity_service)
        self.ui.pushButton_7.clicked.connect(self.reward_service)
        self.ui.pushButton_2.clicked.connect(self.map_service)
        self.ui.pushButton.clicked.connect(self.challenge_service)
        self.ui.pushButton_3.clicked.connect(self.register_meal_service)
        self.ui.pushButton_4.clicked.connect(self.weekly_progress_service)
        self.show()

    def weekly_progress_service(self):
        self.deleteLater()
        db = DBManager()
        self.weekly_progress_obj = WeeklyProgressService(db)
        self.weekly_progress_obj.weekly_progress()

    def register_meal_service(self):
        self.deleteLater()
        db = DBManager()
        supermarket = Supermarket()
        self.register_meal_obj = RegisterMealService(db, supermarket)
        self.register_meal_obj.register_food()

    def map_service(self):
        self.deleteLater()
        self.map_service_obj = MapService()
        self.map_service_obj.find_route()
        self.ui.pushButton_7.clicked.connect(self.challenge_service)
        self.ui.pushButton_5.clicked.connect(self.food_plan_service)
        self.show()

    def food_plan_service(self):
        self.deleteLater()
        food_plan_obj = FoodPlannerService()
        food_plan_obj.createFoodPlanService()

    
    def monitor_activity_service(self):
        self.deleteLater()
        db = DBManager()
        smartwatch = SmartWatch()
        monitor_activity_obj = ActivityMonitorService(db, smartwatch)
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