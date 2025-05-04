from support_classes import Timer, DBManager
from models.Offer import Offer 
from models.CouponCode import CouponCode
from screens.Notification import NotificationScreen 
from screens.RedeemPoints import RedeemPointsScreen
from screens.Confirm import ConfirmScreen
from screens.CouponCode import CouponCodeScreen
import main_menu

class RewardService:
    def __init__(self, db:DBManager):
        self.db = db

    # when the user clicks on "Redeem points" from the main menu
    def get_offers(self):
        
        try:
            offers = self.fetch_offers_from_API()
            if len(offers) <= 0:
                raise ValueError("No offers found")

            rScreen = RedeemPointsScreen()
            rScreen.show()

        except Exception as e:
            error_message = f"Failed to retrieve offers: {str(e)}"
            nScreen = NotificationScreen(error_message)
            nScreen.show()


    # when the user selects the offer & number of times to redeem the offer from the RedeemPointsScreen
    def redeem_offer(self,offer: Offer):
            
        try: 
            rScreen = ConfirmScreen()
            rScreen.show()

            # if he agrees proceed with : 
            self.check_if_offer_valid(offer)
            self.compare_redeem_limit(offer)


            user_points = self.db.get_user_points()

            if user_points - offer.points < 0:
                raise ValueError("Not enough points to redeem")
                
            remaining = user_points - offer.points
            ccode = CouponCode(offer)
            self.db.save_coupon_code(ccode)

            coupon_codes = self.db.get_all_coupon_codes()

            cScreen = CouponCodeScreen()
            cScreen.show()


        except Exception as e:
            error_message = f"Failed to redeem offer: {str(e)}"
            nScreen = NotificationScreen(error_message)
            nScreen.show()

        



    def fetch_offers_from_API() -> list[Offer]:
        pass

    def check_if_offer_valid(offer: Offer):
        pass

    def compare_redeem_limit(offer: Offer):
        pass


    def reward_points_to_user(self,points:int) ->int:
        pass

