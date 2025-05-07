from screens.FoodInformationScreen import FoodInformationScreen
from screens.RecentlyScannedScreen import RecentlyScannedScreen
from models.DBManager import DBManager
from models.Edible import Edible
from models.Image import Image
from models.CameraService import CameraService


class ImageUploadService():

    def __init__(self, db:DBManager):
        self.db = db

    def get_image_from_camera(self):
        pass

    def check_for_clarity(self):
        pass

    def get_QR(self):
        pass

    def match_image_to_food(self):
        pass

    def show_food_confirmation(self):
        self.food_confirmation_screen = FoodConfirmationScreen(self)
        self.food_confirmation_screen.show()

    def food(self):
        pass