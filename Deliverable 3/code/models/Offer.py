import datetime

class Offer:
    def __init__(self,points,description,validTill,redeemLimit):
        self.points = points
        self.description = description
        self.RedeemLimit = redeemLimit
        self.validTill = validTill
    