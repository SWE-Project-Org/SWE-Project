from PyQt6.QtWidgets import QWidget
from screens.CouponCode import CouponCodeScreen
from ui_py import (redeem_points_ui)
from models.Offer import Offer
import main_menu

class RedeemPointsScreen(QWidget):
    def __init__(self,service):
        super().__init__()
        self.ui = redeem_points_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.show_voucher_screen) #My vouchers
        self.ui.pushButton_6.clicked.connect(self.select_offer_from_screen) #first coupon
        self.ui.pushButton_7.clicked.connect(self.select_offer_from_screen) #second
        self.ui.pushButton_8.clicked.connect(self.select_offer_from_screen) #third
        self.ui.pushButton_9.clicked.connect(self.select_offer_from_screen) #fourth
        self.ui.pushButton_10.clicked.connect(self.select_offer_from_screen) #fifth
        self.ui.pushButton_11.clicked.connect(self.show_main_menu_screen) #back
        self.ui.pushButton_12.clicked.connect(self.redeem_offer) #redeem

    def redeem_offer(self):
        # Get the selected offer and number of times to redeem
        offer = self.select_offer_from_screen()
        times = self.get_number_of_times_to_redeem()

        self.service.redeem_offer(offer,times)

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()

    def show_voucher_screen(self):
        self.deleteLater()
        self.cScreen = CouponCodeScreen(self)
        self.cScreen.show()

    def select_offer_from_screen(self) -> Offer:
        return Offer(points=100,description="Test Offer",validTill="2023-12-31",redeemLimit=5)

    def get_number_of_times_to_redeem(self) -> int:
        return 1