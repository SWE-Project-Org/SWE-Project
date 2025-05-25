from models.Map import Map
from models.Route import Route
from models.Location import Location
from screens.ChoiceEntryScreen import ChoiceEntryScreen
from screens.RouteSelectionScreen import RouteSelectionScreen
from screens.RouteDisplayScreen import RouteDisplayScreen

class MapService:
    def __init__(self):
        self.choices = 'route choices'
        self.map = None
        self.locations = None

    def find_route(self):
        self.map = self.get_map()
        self.choice_entry_screen = ChoiceEntryScreen(self)
        self.choice_entry_screen.show()

    def returned_choice(self, choice):
        if choice == None:
            self.route_selection_screen = RouteSelectionScreen(self, self.routes)
            self.route_selection_screen.show()
        else:
            self.choices = choice
            distance = self.estimate_distance()
            print(distance)
            self.check_realistic(distance)
            self.locations = self.get_locations()
            self.routes = self.get_routes(distance)
            self.route_selection_screen = RouteSelectionScreen(self, self.routes)
            self.route_selection_screen.show()

    def show_selected_route(self, selected_route):
        self.route_display_screen = RouteDisplayScreen(self, selected_route)
        self.route_display_screen.show()

    def estimate_distance(self):
        return self.choices[2] / 60

    def check_realistic(self, distance):
        if distance > 30:
            print("unrealistic")

    def get_map(self):
        return Map()

    def get_locations(self):
        return ['b', 'c', 'd']

    def get_routes(self, distance):
        return [Route(self.choices[1], self.locations[0], int(distance*6), self.choices[2]), 
                Route(self.choices[1], self.locations[1], int(distance*6), self.choices[2]), 
                Route(self.choices[1], self.locations[2], int(distance*6), self.choices[2])]

    

    