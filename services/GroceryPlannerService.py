from models.Supermarket import Supermarket
from models.Ingredients import Ingredients
from models.DBManager import DBManager
from screens.FoodPlanSummaryScreen import FoodPlanSummaryScreen
from screens.Notification import NotificationScreen



class GroceryPlannerService:
    def __init__(self, db: DBManager, supermarket: Supermarket):
        self.db = db
        self.supermarket = supermarket
        
    def createGroceryService(self, budget: float):
        self.budget = budget
        ingredients = self.analyzeMeals()
        ingredients_obj = self.createIngredients(ingredients)
        getFoodAvailability = self.getFoodAvailability()
        total_cost = self.calculateFoodCost(getFoodAvailability)
        if not self.compareCostwBudget(total_cost, budget):
            self.notification = NotificationScreen("Budget Exceeded", "The total cost exceeds your budget.")
            self.notification.show()
            return
        ingredient_list = self.storeIngredientList(ingredients_obj)

        self.create_grocery_planner_screen = FoodPlanSummaryScreen(self)
        self.create_grocery_planner_screen.show()

    def createIngredients(self, ingredients):
        ingredients_obj = Ingredients(ingredients)
        return ingredients_obj

    def analyzeMeals(self):
         return [('Chicken', 500), 
                ('Potatoes', 300), 
                ('Beef', 600), 
                ('Cheese', 400), 
                ('Salad', 100)]
        
    def getFoodAvailability(self):
        return self.supermarket.getFoodAvailabilty()
    
    def calculateFoodCost(self, getFoodAvailability):
        if not getFoodAvailability:
            return False
        
        total_cost = 0
        total_cost = sum(self.supermarket.fetch_prices())

        return total_cost
    
    def compareCostwBudget(self, total_cost, budget):
        if total_cost <= budget:
            return True
        else:
            return False
        
    def storeIngredientList(self, ingredients:  Ingredients):
       
       return self.db.storeIngredientList(ingredients)
    
    