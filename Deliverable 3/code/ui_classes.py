from PyQt6.QtWidgets import QWidget
from ui_py import (select_activity_ui, activity_monitor_ui, activity_summary_ui,
                    scan_qr_ui, confirm_food_ui, food_info_ui,
                    daily_challenge_ui,
                    find_route_ui, select_route_ui, route_result_ui,
                    my_vouchers_ui, redeem_points_ui)
import main_menu
  

class ActivitySelectionScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = select_activity_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_9.clicked.connect(self.service_create_activity)
        self.ui.pushButton_10.clicked.connect(self.service_create_activity)
        self.ui.pushButton_11.clicked.connect(self.show_main_menu_screen)

    def service_create_activity(self):
        self.deleteLater()
        self.service.create_activity()

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()


class ActivityMonitorScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = activity_monitor_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton_9.clicked.connect(self.service_end_activity)
        
    def service_end_activity(self):
        self.deleteLater()
        self.service.end_activity()

    def update(self):
        pass


class ActivitySummaryScreen(QWidget):
    def __init__(self, service):
        super().__init__()
        self.ui = activity_summary_ui.Ui_Form()
        self.ui.setupUi(self)
        self.service = service
        self.ui.pushButton_9.clicked.connect(self.show_main_menu_screen)

    def show_main_menu_screen(self):
        self.deleteLater()
        self.main_menu = main_menu.MainMenuScreen()

    
def placeholder():
    pass


class FoodConfirmationScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = confirm_food_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_10.clicked.connect(placeholder) #
        self.ui.pushButton_9.clicked.connect(placeholder) #

class RecentlyScannedScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = scan_qr_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_11.clicked.connect(placeholder) #
        self.ui.pushButton_5.clicked.connect(placeholder) #

class FoodInfoScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = food_info_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_9.clicked.connect(placeholder) #


class DailyChallengeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = daily_challenge_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(placeholder) #
        self.ui.pushButton_6.clicked.connect(placeholder) #
        self.ui.pushButton_11.clicked.connect(placeholder) #


class ChoiceRouteScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = find_route_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(placeholder) #
        self.ui.pushButton_6.clicked.connect(placeholder) #
        self.show()


class RouteSelectionScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = select_route_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(placeholder) #
        self.ui.pushButton_3.clicked.connect(placeholder) #
        self.ui.pushButton.clicked.connect(placeholder) #
        self.ui.pushButton_8.clicked.connect(placeholder) #

class RouteDisplayScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = route_result_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_8.clicked.connect(placeholder) #
        self.ui.pushButton_9.clicked.connect(placeholder) #
    

class RedeemPointsScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = redeem_points_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(placeholder) #My vouchers
        self.ui.pushButton_6.clicked.connect(placeholder) #first coupon
        self.ui.pushButton_7.clicked.connect(placeholder) #second
        self.ui.pushButton_8.clicked.connect(placeholder) #third
        self.ui.pushButton_9.clicked.connect(placeholder) #fourth
        self.ui.pushButton_10.clicked.connect(placeholder) #fifth
        self.ui.pushButton_11.clicked.connect(placeholder) #back
        self.ui.pushButton_12.clicked.connect(placeholder) #redeem



class CouponCodeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = my_vouchers_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_6.clicked.connect(placeholder) #back button


