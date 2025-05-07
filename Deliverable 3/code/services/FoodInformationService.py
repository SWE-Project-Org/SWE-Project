from screens.FoodInformationScreen import FoodInformationScreen
from screens.RecentlyScannedScreen import RecentlyScannedScreen
from models.DBManager import DBManager
from models.RecentlyScannedFood import RecentlyScannedFood
from models.SupermarketAPI import SupermarketAPI


class FoodInformationService():

    def __init__(self):
        pass
    
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

    def get_food_info(self):
        #Εδώ καλούνται όλες οι παραπάνω μεθοδοί
        self.food_information_screen = FoodInformationScreen(self)
        self.food_information_screen.show()
        #μετά καλούνται όλες οι παρακάτω μεθόδοι

    def save_recently_scanned_food(self):
        pass
    
    def get_recently_scanned_foods(self):
        pass

    def show_recently_scanned(self):
        self.recently_scanned_screen = RecentlyScannedScreen(self)
        self.recently_scanned_screen.show()
