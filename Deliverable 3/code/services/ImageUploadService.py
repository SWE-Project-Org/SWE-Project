from screens.FoodConfirmationScreen import FoodConfirmationScreen
from models.DBManager import DBManager
from models.Edible import Edible
from models.Image import Image
from models.Camera import Camera


class ImageUploadService():
    def __init__(self, db: DBManager, camera: Camera, food_info_service):
        self.camera = camera
        self.db = db
        self.food_info_service = food_info_service

    def get_image(self):
        image = Image(self.camera.get_image_from_camera())
        self.check_for_clarity(image)
        self.get_QR(image)
        matched_food = self.db.match_image_to_food()
        edible = Edible(matched_food)            
        self.food_confirmation_screen = FoodConfirmationScreen(self.food_info_service)
        self.food_confirmation_screen.show()

    def check_for_clarity(self, image):
        pass

    def get_QR(self, image):
        pass

    

