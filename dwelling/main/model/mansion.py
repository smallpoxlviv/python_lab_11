import location
from abstract_dwelling import AbstractDwelling 
class Mansion(AbstractDwelling):
    def __init__(self, area_in_square_meters = 0, price_in_USD = 0, location = location.Location(),\
        district = "Shwadchack", balcony_count = 0, area_of_land_in_squareMeters = 0, entrance_door_count = 0, other_buildings_in_area = False):
        super().__init__(area_in_square_meters, price_in_USD, location, district, balcony_count)
        self.area_of_land_in_squareMeters = area_of_land_in_squareMeters
        self.entrance_door_count = entrance_door_count
        self.other_buildings_in_area = other_buildings_in_area
        