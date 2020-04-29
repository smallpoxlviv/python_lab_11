from abc import ABC
from abc import abstractmethod
import location
import math

class AbstractDwelling(ABC):
    @abstractmethod
    def __init__ (self, area_in_square_meters = 0, price_in_USD = 0, location = location.Location(),\
        district = "Shwadchack", balcony_count = 0):
        self.area_in_square_meters = area_in_square_meters
        self.price_in_USD = price_in_USD
        self.location = location
        self.district = district
        self.balcony_count = balcony_count

    def calculate_distance_to_closer_school_in_meters(self, list_of_location):
        smallest_distance =  math.sqrt(((list_of_location[0].x_in_decimal_degrees - self.location.x_in_decimal_degrees) ** 2)\
            + ((list_of_location[0].y_in_decimal_degrees - self.location.y_in_decimal_degrees) ** 2))
        for location in list_of_location:
            distance = math.sqrt(((location.x_in_decimal_degrees - self.location.x_in_decimal_degrees) ** 2)\
                    + ((location.y_in_decimal_degrees - self.location.y_in_decimal_degrees) ** 2))
            if (distance < smallest_distance):
                smallest_distance = distance
        return smallest_distance * 111000            

    def calculate_distance_to_closer_kindergarden_in_meters(self, list_of_location):
        smallest_distance =  math.sqrt(((list_of_location[0].x_in_decimal_degrees - self.location.x_in_decimal_degrees) ** 2)\
            + ((list_of_location[0].y_in_decimal_degrees - self.location.y_in_decimal_degrees) ** 2))
        for location in list_of_location:
            distance = math.sqrt(((location.x_in_decimal_degrees - self.location.x_in_decimal_degrees) ** 2)\
                    + ((location.y_in_decimal_degrees - self.location.y_in_decimal_degrees) ** 2))
            if (distance < smallest_distance):
                smallest_distance = distance
        return smallest_distance * 111000 
    
    def calculate_distance_to_closer_playground_in_meters(self, list_of_location):
        smallest_distance =  math.sqrt(((list_of_location[0].x_in_decimal_degrees - self.location.x_in_decimal_degrees) ** 2)\
            + ((list_of_location[0].y_in_decimal_degrees - self.location.y_in_decimal_degrees) ** 2))
        for location in list_of_location:
            distance = math.sqrt(((location.x_in_decimal_degrees - self.location.x_in_decimal_degrees) ** 2)\
                    + ((location.y_in_decimal_degrees - self.location.y_in_decimal_degrees) ** 2))
            if (distance < smallest_distance):
                smallest_distance = distance
        return smallest_distance * 111000 
