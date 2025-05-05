from models.Supermarket import SupermarketAPI
from models.Ingredients import Ingredients
from models.DBManager import DBManager
from screens.FoodPlanSummaryScreen import FoodPlanSummaryScreen


class GroceryPlannerService:

    def __init__(self):
      pass
    
    def createGroceryService(self):
        self.create_grocery_planner_screen = FoodPlanSummaryScreen(self)
        self.create_grocery_planner_screen.show()

    def analyzeMeals(self):
        pass

    def getFoodAvailability(self):
        pass

    def calculateFoodCost(self):
        pass
    def createCostwBudget(self):
        pass
    def storeIngredientList(self):
        pass