import location
from abstract_dwelling import AbstractDwelling 
class Penthouse(AbstractDwelling):
    def __init__(self, area_in_square_meters = 0, price_in_USD = 0, location = location.Location(),\
        district = "Shwadchack", balcony_count = 0):
        AbstractDwelling.__init__(area_in_square_meters, price_in_USD, location,\
        district, balcony_count)