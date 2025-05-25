def placeholder():
    pass


from PyQt6.QtWidgets import QWidget
from ui_py import select_route_ui
import main_menu

class RouteSelectionScreen(QWidget):
    def __init__(self, service, routes):
        super().__init__()
        self.ui = select_route_ui.Ui_Form()
        self.service = service
        self.ui.setupUi(self)
        self.ui.pushButton.setText(routes[0].start + " - " + routes[0].dest + ",\n"
                                   + str(routes[0].time) + "min" + ", " + str(routes[0].cal) + "kcal")
        self.ui.pushButton_2.setText(routes[1].start + " - " + routes[1].dest + ",\n"
                                   + str(routes[1].time) + "min" + ", " + str(routes[1].cal) + "kcal")
        self.ui.pushButton_3.setText(routes[2].start + " - " + routes[2].dest + ",\n"
                                   + str(routes[2].time) + "min" + ", " + str(routes[2].cal) + "kcal")
        self.ui.pushButton_2.clicked.connect(self.service_show_selected_route2)
        self.ui.pushButton_3.clicked.connect(self.service_show_selected_route3)
        self.ui.pushButton.clicked.connect(self.service_show_selected_route1)
        self.ui.pushButton_8.clicked.connect(self.back_to_find_route)


    def service_show_selected_route1(self):
        self.deleteLater()
        self.service.show_selected_route(0)

    def service_show_selected_route2(self):
        self.deleteLater()
        self.service.show_selected_route(1)

    def service_show_selected_route3(self):
        self.deleteLater()
        self.service.show_selected_route(2)

    def back_to_find_route(self):
        self.deleteLater()
        self.service.find_route()


    

    

