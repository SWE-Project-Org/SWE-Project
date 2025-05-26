from PyQt6.QtWidgets import QMainWindow
from ui_py import (main_menu_ui)

from instanciation import register_meal_service,weekly_progress_service,map_service
from instanciation import food_planner_service,activity_monitor_service,reward_service,challenge_service,image_upload_service, food_information_service
from instanciation import db

class MainMenuScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_menu_ui.Ui_MainWindow()  
        self.ui.setupUi(self) 
        self.ui.label_5.setText(str(db.get_consumed_calories())) #consumed
        self.ui.label_6.setText(str(db.get_burned_calories())) #burned
        self.ui.label_7.setText(str(db.get_daily_limit())) #goal
        self.ui.label_8.setText(str(db.get_calorie_counter())) #goal
        self.ui.pushButton_8.clicked.connect(self.on_click_monitor_activity_btn)
        self.ui.pushButton_7.clicked.connect(self.on_click_redeem_points_btn)
        self.ui.pushButton_2.clicked.connect(self.on_click_route_btn)
        self.ui.pushButton.clicked.connect(self.on_click_challenge_btn)
        self.ui.pushButton_3.clicked.connect(self.on_click_register_meal_btn)
        self.ui.pushButton_4.clicked.connect(self.on_click_weekly_progress_btn)
        self.ui.pushButton_5.clicked.connect(self.on_click_create_food_plan_btn)
        self.ui.pushButton_6.clicked.connect(self.on_click_food_information_btn)

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

    def on_click_weekly_progress_btn(self):
        self.deleteLater()
        self.weekly_progress_obj.weekly_progress()

    def on_click_register_meal_btn(self):
        self.deleteLater()
        self.register_meal_obj.register_food()

    def on_click_route_btn(self):
        self.deleteLater()
        self.map_service_obj.find_route()

    def on_click_create_food_plan_btn(self):
        self.deleteLater()
        self.food_plan_obj.createFoodPlanService()
    
    def on_click_monitor_activity_btn(self):
        self.deleteLater()
        self.monitor_activity_obj.monitor_activity()

    def on_click_challenge_btn(self):
        self.deleteLater()
        self.challenge_service.start_daily_challenge()

    def on_click_food_information_btn(self):
        self.deleteLater()
        self.food_information_service.food_info()

    def on_click_redeem_points_btn(self):
        self.deleteLater()
        self.reward_service.get_offers()


