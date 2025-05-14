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
        self.choices = choice
        self.estimate_distance()
        self.check_realistic()
        self.locations = self.get_locations()
        self.routes = self.get_routes()
        self.route_selection_screen = RouteSelectionScreen(self)
        self.route_selection_screen.show()

    def show_selected_route(self):
        self.route_display_screen = RouteDisplayScreen(self)
        self.route_display_screen.show()

    def estimate_distance(self):
        pass

    def check_realistic(self):
        pass

    def get_map(self):
        return Map()

    def get_locations(self):
        return Location()

    def get_routes(self):
        return Route()

    

    