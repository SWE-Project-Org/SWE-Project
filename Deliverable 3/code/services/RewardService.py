import datetime
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

            self.rScreen = RedeemPointsScreen(self)
            self.rScreen.show()

        except Exception as e:
            error_message = f"Failed to retrieve offers: {str(e)}"
            print(error_message)
            # self.nScreen = NotificationScreen(self,error_message)
            # self.nScreen.show()


    # when the user selects the offer & number of times to redeem the offer from the RedeemPointsScreen
    def redeem_offer(self,offer: Offer,index,times):
            
        try: 
            # self.rScreen = ConfirmScreen()
            # self.rScreen.show()

            # if he agrees proceed with : 
            # self.check_if_offer_valid(offer)
            # self.compare_redeem_limit(offer,times)


            # user_points = self.db.get_user_points()

            # if user_points - offer.points < 0:
            #     raise ValueError("Not enough points to redeem")
                
            # remaining = user_points - offer.points
            # ccode = CouponCode(offer)
            # self.db.save_coupon_code(ccode)

            # coupon_codes = self.db.get_all_coupon_codes()

            self.cScreen = CouponCodeScreen(self)
            self.cScreen.show()


        except Exception as e:
            error_message = f"Failed to redeem offer: {str(e)}"
            print(error_message)
            self.nScreen = NotificationScreen(self,error_message)
            self.nScreen.show()

        



    def fetch_offers_from_API(self) -> list[Offer]:
        return [
            Offer(
            points=100,
            description="Masoutis",
            validTill=datetime.datetime.now() + datetime.timedelta(days=30),
            redeemLimit=5
            ),
            Offer(
            points=200,
            description="Sklavenitis",
            validTill=datetime.datetime.now() + datetime.timedelta(days=60),
            redeemLimit=2
            ),
            Offer(
            points=50,
            description="MyMarket",
            validTill=datetime.datetime.now() + datetime.timedelta(days=15),
            redeemLimit=10
            ),
            Offer(
            points=500,
            description="Lidl",
            validTill=datetime.datetime.now() + datetime.timedelta(days=90),
            redeemLimit=1
            )
        ]

    def check_if_offer_valid(self,offer: Offer):
        pass

    def compare_redeem_limit(self,offer: Offer,times):
        pass


    def reward_points_to_user(self,points:int) ->int:
        pass

