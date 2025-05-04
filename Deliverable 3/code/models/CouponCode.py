import datetime
from Offer import Offer

class CouponCode:
    def __init__(self,offer: Offer):
        self.code = ""
        self.description = ""
        self.validTill = datetime.datetime.now()
