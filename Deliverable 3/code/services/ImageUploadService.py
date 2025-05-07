from screens.FoodConfirmationScreen import FoodConfirmationScreen
from models.DBManager import DBManager
from models.Edible import Edible
from models.Image import Image
from models.CameraAPI import CameraAPI


class ImageUploadService():

    def __init__(self):
        pass

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