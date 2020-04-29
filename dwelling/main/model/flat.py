import location
from abstract_dwelling import AbstractDwelling 
class Flat(AbstractDwelling):
    def __init__(self, area_in_square_meters = 0, price_in_USD = 0, location = location.Location(),\
        district = "Shwadchack", balcony_count = 0, neighboring_apartments_on_floor_count = 0):
        AbstractDwelling.__init__(area_in_square_meters, price_in_USD, location,\
        district, balcony_count)
        self.neighboring_apartments_on_floor_count = neighboring_apartments_on_floor_count