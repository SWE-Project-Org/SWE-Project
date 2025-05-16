from screens.ScanQRScreen import ScanQRScreen
from screens.FoodInformationScreen import FoodInformationScreen
from models.DBManager import DBManager
from models.RecentlyScannedFood import RecentlyScannedFood
from models.Supermarket import Supermarket

class FoodInformationService():
    def __init__(self, db: DBManager, supermarket: Supermarket, image_upload_service):
        self.db = db
        self.supermarket = supermarket
        self.recently_scanned_foods = None
        self.image_upload_service = image_upload_service
    
    def food_info(self):
        self.recently_scanned_foods = self.db.get_recently_scanned_foods()
        self.scan_qr_screen = ScanQRScreen(self.image_upload_service)
        self.scan_qr_screen.show()

    def get_food_info(self):
        info = self.db.get_info()
        ingredients = self.db.get_ingredients()
        allergies = self.db.get_allergies()
        self.check_for_allergies(allergies, ingredients)
        rating = self.rate_dietary_value()
        prices = self.db.fetch_prices()
        self.food_information_screen = FoodInformationScreen(self)
        self.food_information_screen.show()
        
    def food_info_done(self):
        from main_menu import MainMenuScreen
        recently_scanned_food = RecentlyScannedFood()
        self.db.save_recently_scanned_food(recently_scanned_food)
        self.main_menu = MainMenuScreen()

    def check_for_allergies(self, allergies, ingredients):
        pass

    def rate_dietary_value(self):
        return 4






