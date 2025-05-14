import datetime
from models.Offer import Offer

class CouponCode:
    def __init__(self,offer: Offer):
        self.offer = offer  
        self.code = ""
        self.description = ""
        self.validTill = datetime.datetime.now()
