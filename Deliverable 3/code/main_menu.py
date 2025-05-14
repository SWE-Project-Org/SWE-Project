from PyQt6.QtWidgets import QMainWindow
from ui_py import (main_menu_ui)

from instanciation import register_meal_service,weekly_progress_service,map_service
from instanciation import food_planner_service,activity_monitor_service,reward_service,challenge_service,image_upload_service, food_information_service


class MainMenuScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_menu_ui.Ui_MainWindow()  
        self.ui.setupUi(self) 
        # buttons from the main screen
        self.ui.pushButton_8.clicked.connect(self.monitor_activity_service)
        self.ui.pushButton_7.clicked.connect(self.reward_service)
        self.ui.pushButton_2.clicked.connect(self.map_service)
        self.ui.pushButton.clicked.connect(self.challenge_service)
        self.ui.pushButton_3.clicked.connect(self.register_meal_service)
        self.ui.pushButton_4.clicked.connect(self.weekly_progress_service)
        self.ui.pushButton_5.clicked.connect(self.food_plan_service)
        self.ui.pushButton_6.clicked.connect(self.food_information_service)

        self.weekly_progress_obj = weekly_progress_service
        self.register_meal_obj = register_meal_service
        self.map_service_obj = map_service
        self.food_plan_obj = food_planner_service
        self.monitor_activity_obj = activity_monitor_service
        self.challenge_service = challenge_service
        self.image_upload_service = image_upload_service
        self.reward_service = reward_service
        self.food_information_service = food_information_service
        self.show()

    def weekly_progress_service(self):
        self.deleteLater()
        self.weekly_progress_obj.weekly_progress()

    def register_meal_service(self):
        self.deleteLater()
        self.register_meal_obj.register_food()

    def map_service(self):
        self.deleteLater()
        self.map_service_obj.find_route()

    def food_plan_service(self):
        self.deleteLater()
        self.food_plan_obj.createFoodPlanService()

    
    def monitor_activity_service(self):
        self.deleteLater()
        self.monitor_activity_obj.monitor_activity()

    def challenge_service(self):
        self.deleteLater()
        self.challenge_service.start_daily_challenge()

    def food_information_service(self):
        self.deleteLater()
        self.food_information_service.food_info()

    def reward_service(self):
        self.deleteLater()
        self.reward_service.get_offers()
