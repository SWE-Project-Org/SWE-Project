from models.SmartWatch import SmartWatch
from models.Supermarket import Supermarket
from services.RewardService import RewardService
from services.ActivityMonitorService import ActivityMonitorService
from services.ChallengeService import ChallengeService
from services.FoodPlannerService import FoodPlannerService
from services.ImageUploadService import ImageUploadService
from services.MapService import MapService
from services.RegisterMealService import RegisterMealService
from services.WeeklyProgressService import WeeklyProgressService
from models.DBManager import  DBManager

db = DBManager()
smartwatch = SmartWatch() # smartwatch API service
supermarket = Supermarket() # supermarket API service
        
register_meal_service = RegisterMealService(db, supermarket)
weekly_progress_service = WeeklyProgressService(db)
map_service = MapService()
food_planner_service = FoodPlannerService()
activity_monitor_service = ActivityMonitorService(db, smartwatch)

reward_service = RewardService(db)
challenge_service = ChallengeService(db,reward_service)

image_upload_service = ImageUploadService()
