from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt
from screens.CouponCode import CouponCodeScreen
from ui_py import (redeem_points_ui)
from models.Offer import Offer
import main_menu

class RedeemPointsScreen(QWidget):
    def __init__(self, service, offers):
        super().__init__()
        self.ui = redeem_points_ui.Ui_Form()
        self.service = service
        self.offers = offers
        self.selected_offer_index = 0
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.show_voucher_screen) # My vouchers
        self.ui.pushButton_11.clicked.connect(self.show_main_menu_screen) # back
        self.ui.pushButton_12.clicked.connect(self.redeem_offer) # redeem

        # Offer labels
        self.offer_labels = [self.ui.label_8, self.ui.label_9, self.ui.label_10, self.ui.label_11]
        self.combo_boxes = [self.ui.comboBox_3, self.ui.comboBox_4, self.ui.comboBox_5, self.ui.comboBox_6]
        for i, label in enumerate(self.offer_labels):
            if i < len(self.offers):
                offer = self.offers[i]
                label.setText(f"{offer.description}, {offer.points}pt -> Redeem Limit: {offer.redeemLimit}")
                label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
                label.mousePressEvent = self.make_label_click_handler(i)
            else:
                label.hide()
        self.highlight_selected_offer()

        # Update My Points label with actual value from DB
        points = self.service.db.get_user_points()
        self.ui.label_12.setText(f"My Points:\n{points}")

    def make_label_click_handler(self, idx):
        def handler(event):
            self.selected_offer_index = idx
            self.highlight_selected_offer()
        return handler

    def redeem_offer(self):
        offer = self.offers[self.selected_offer_index]
        combo = self.combo_boxes[self.selected_offer_index]
        times = int(combo.currentText())
        if times <= 0:
            # Optionally show a message to select at least 1
            return
        self.service.redeem_offer(offer, times)

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()

    def show_voucher_screen(self):
        self.deleteLater()
        self.cScreen = CouponCodeScreen(self, self.service.db.get_all_coupon_codes())
        self.cScreen.show()

    def select_offer_from_screen(self) -> Offer:
        # Example: select offer based on which comboBox is non-zero
        # This is a placeholder logic, you can improve it as needed
        offers = [
            Offer(points=1500, description="Masoutis, 1500pt -> 4$", validTill="2023-12-31", redeemLimit=1),
            Offer(points=1500, description="AB, 1500pt -> 4$", validTill="2023-12-31", redeemLimit=1),
            Offer(points=1500, description="Sklavenitis, 1500pt -> 4$", validTill="2023-12-31", redeemLimit=1),
            Offer(points=1500, description="Galaxias, 1500pt -> 4$", validTill="2023-12-31", redeemLimit=1),
        ]
        combo_boxes = [self.ui.comboBox_3, self.ui.comboBox_4, self.ui.comboBox_5, self.ui.comboBox_6]
        for i, cb in enumerate(combo_boxes):
            if cb.currentIndex() > 0:
                return offers[i]
        # Default to first offer if none selected
        return offers[0]

    def get_number_of_times_to_redeem(self) -> int:
        # Return the number selected in the first non-zero combo box
        combo_boxes = [self.ui.comboBox_3, self.ui.comboBox_4, self.ui.comboBox_5, self.ui.comboBox_6]
        for cb in combo_boxes:
            if cb.currentIndex() > 0:
                return cb.currentIndex()
        return 1

    def highlight_selected_offer(self):
        for i, label in enumerate(self.offer_labels):
            if i == self.selected_offer_index:
                label.setStyleSheet("background-color: #e0e0e0; color: #e91e63; border-radius: 6px; padding: 5px;")
            else:
                label.setStyleSheet("color: #000; background-color: #00000000; border-radius: 6px; padding: 5px;")