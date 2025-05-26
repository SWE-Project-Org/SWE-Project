from screens.RegisterMealScreen import RegisterMealScreen
from models.Supermarket import Supermarket
from models.RegisteredFood import RegisteredFood
from models.DBManager import  DBManager


class RegisterMealService:
    def __init__(self, db:DBManager, supermarket:Supermarket):
        self.db = db
        self.supermarket = supermarket
        self.registered_food = None

    def register_food(self):
        food_list = self.supermarket.get_food_list()

        self.resiger_meal_screen = RegisterMealScreen(self, food_list)
        self.resiger_meal_screen.show()

    def create_registered_food(self):
        self.registered_food = RegisteredFood()
        exceeded = self.db.update_calorie_counter()
        self.store_food()
        self.register_food()

    def store_food():
        pass





