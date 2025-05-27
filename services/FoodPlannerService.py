from ui_py.create_food_plan_ui import Ui_Form
from models.Supermarket import Supermarket
from models.FoodPlan import FoodPlan
from screens.CreateFoodPlanScreen import CreateFoodPlanScreen
from screens.GroceryPlannerScreen import CreateGroceryPlannerScreen
from services.GroceryPlannerService import GroceryPlannerService
from models.DBManager import DBManager


class FoodPlannerService:

    def __init__(self, db: DBManager, supermarket: Supermarket):
        self.db = db
        self.supermarket = supermarket

    def createFoodPlanService(self):
        self.create_food_plan_screen = CreateFoodPlanScreen(self)
        self.create_food_plan_screen.show()
        

    def enterGoal(self):
        #self.desired_goal = input()
        self.grocery_planner_screen = CreateGroceryPlannerScreen(self)
        self.grocery_planner_screen.show()

    def goalAssess(self,goal:str):
        pass
    def getFoodList(self):
        pass
    def createFoodPlan(self,goal:str,foodplan:FoodPlan):
        pass
    


