from models.Supermarket import SupermarketAPI
from models.Ingredients import Ingredients
from models.DBManager import DBManager
from FoodPlannerService import FoodPlannerService


class GroceryPlannerService:

    def __init__(self, sm: SupermarketAPI,foodplanner:FoodPlannerService,db:DBManager):
        self.db = db
        self.sm = sm
        self.foodplanner = foodplanner

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