import datetime
from models.Offer import Offer

class CouponCode:
    def __init__(self, offer: Offer):
        self.offer = offer
        # Generate a random coupon code using timestamp and offer details
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.code = f"COUPON-{timestamp}-{hash(offer.description)}"[:16]
        self.description = offer.description
        if isinstance(offer.validTill, str):
            self.validTill = datetime.datetime.strptime(offer.validTill, "%Y-%m-%d")
        else:
            self.validTill = offer.validTill
