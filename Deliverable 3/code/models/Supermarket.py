import datetime
from .Offer import Offer

class Supermarket:
    def __init__(self):
        pass
    def get_food_list():
        return list()

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