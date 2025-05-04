import datetime

class Offer:
    def __init__(self):
        self.points = 0
        self.description = ""
        self.RedeemLimit = 2
        self.validTill = datetime.datetime.now()
    