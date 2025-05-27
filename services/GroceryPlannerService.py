from models.Supermarket import Supermarket
from models.Ingredients import Ingredients
from models.DBManager import DBManager
from screens.FoodPlanSummaryScreen import FoodPlanSummaryScreen


class GroceryPlannerService:
    def __init__(self, db: DBManager, supermarket: Supermarket):
        self.db = db
        self.supermarket = supermarket
    
    def createGroceryService(self):
        self.create_grocery_planner_screen = FoodPlanSummaryScreen(self)
        self.create_grocery_planner_screen.show()

    def analyzeMeals(self):
        pass

    def calculateFoodCost(self):
        pass
    
    def createCostwBudget(self):
        pass
    