from location import Location 

class CityInfrastructure:
    def __init__(self):
        self.locations_of_schools = []
        self.locations_of_kindergardens = []
        self.locations_of_playgrounds = []

    def add_school(self, x_in_decimal_degrees, y_in_decimal_degrees):
        self.locations_of_schools.append(Location(x_in_decimal_degrees, y_in_decimal_degrees))

    def add_kindergarden(self, x_in_decimal_degrees, y_in_decimal_degrees):
        self.locations_of_kindergardens.append(Location(x_in_decimal_degrees, y_in_decimal_degrees))
    
    def add_playground(self, x_in_decimal_degrees, y_in_decimal_degrees):
        self.locations_of_playgrounds.append(Location(x_in_decimal_degrees, y_in_decimal_degrees))