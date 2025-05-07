from screens.FoodInformationScreen import FoodInformationScreen
from screens.RecentlyScannedScreen import RecentlyScannedScreen
from models.DBManager import DBManager
from models.RecentlyScannedFood import RecentlyScannedFood
from models.SupermarketAPI import SupermarketAPI


class FoodInformationService():

    def __init__(self, db:DBManager):
        self.db = db

    def get_info(self):
        pass

    def get_ingredients(self):
        pass

    def get_allergies(self):
        pass

    def check_for_allergies(self):
        pass

    def rate_dietary_value(self):
        pass
    
    def fetch_prices(self):
        pass

    def show_food_information(self):
        self.food_information_screen = FoodInformationScreen(self)
        self.food_information_screen.show()

    def save_recently_scanned_food(self)
        pass
    
    def get_recently_scanned_foods(self)
        pass

    def show_recently_scanned(self):
        self.recently_scanned_screen = RecentlyScannedScreen(self)
        self.recently_scanned_screen.show()

