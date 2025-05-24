from models.Challenge import Challenge


class DBManager:
    def __init__(self):
         pass
    def store_activity(self):
        pass

    def update_calorie_counter(self):
        pass

    def is_daily_challenge_completed(self) -> bool:
        pass

    def save_challenge(self, challenge: Challenge) -> None:
        pass

    def get_user_points(self) -> int:
        pass

    # returns balance
    def subtract_user_points(self) -> int:
        pass

    def update_user_points(self, points: int) -> None:
        pass

    # save the coupon code
    def save_coupon_code(self):
        pass

    def get_all_coupon_codes(self):
        pass

    def get_weekly_data(self):
        return 'weekly data'
    
    def get_recently_scanned_foods(self):
        return 'return_recently_scanned_foods'
    
    def get_info(self):
        return 'info'
    
    def get_ingredients(self):
        return 'ingredients'
    
    def get_allergies(self):
        return 'allergies'
    
    def save_recently_scanned_food(self, recently_scanned_food):
        pass

    def match_image_to_food(self):
        return 'MatchedFood'
    
    def fetch_prices(self):
        return 'prices'
    
    def storeIngredientList(self):
        pass