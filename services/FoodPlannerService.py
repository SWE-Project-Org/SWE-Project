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
        

    def enterGoal(self, goal: str, desired_weight: float):
        if not self.goalAssess(goal, desired_weight):
            self.createFoodPlanService()
            return
        getFoodList = self.getFoodList()
        self.createFoodPlan(goal, getFoodList)
        self.displayGroceryPlannerScreen()

    def goalAssess(self,goal:str, desired_weight: float):
        if goal == "Weight Loss":
            pass
        elif goal == "Muscle Gain":
            pass
        if desired_weight < 60 or desired_weight > 80:
                return False
        else:
            return True

    def getFoodList(self):
        return self.supermarket.get_food_list()
    
    def createFoodPlan(self,goal:str,foodlist:list [tuple]):
        food_plan = FoodPlan(goal, foodlist)
        
    
    def displayGroceryPlannerScreen(self):
        self.grocery_planner_screen = CreateGroceryPlannerScreen(self)
        self.grocery_planner_screen.show()

