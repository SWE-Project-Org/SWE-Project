from models.Supermarket import SupermarketAPI
from models.FoodPlan import FoodPlan

class FoodPlannerService:

    def __init__(self,sm:SupermarketAPI):
        self.sm = sm

    def enterGoal(self):
        pass
    def goalAssess(self,goal:str):
        pass
    def getFoodList(self):
        pass
    def createFoodPlan(self,goal:str,foodplan:FoodPlan):
        pass
    


