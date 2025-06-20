import datetime
from .Offer import Offer

class Supermarket:
    def __init__(self):
        pass

    def get_food_list(self):
        return [('Chicken with potatoes', 830), 
                ('Beef Stew', 300), 
                ('Cheesecake', 321),
                ('Greek Salad', 150)]
       
    def fetch_prices(self):
        return [7.99, 5.49, 3.99, 4.99]

    def fetch_offers_from_API(self) -> list[Offer]:
        return [
            Offer(
            points=100,
            description="Masoutis",
            validTill=datetime.datetime.now() + datetime.timedelta(days=30),
            redeemLimit=1
            ),
            Offer(
            points=200,
            description="Sklavenitis",
            validTill=datetime.datetime.now() + datetime.timedelta(days=60),
            redeemLimit=1
            ),
            Offer(
            points=50,
            description="MyMarket",
            validTill=datetime.datetime.now() + datetime.timedelta(days=15),
            redeemLimit=1
            ),
            Offer(
            points=500,
            description="Lidl",
            validTill=datetime.datetime.now() + datetime.timedelta(days=90),
            redeemLimit=1
            )
        ]
    
    def getFoodAvailabilty(self):
        return True