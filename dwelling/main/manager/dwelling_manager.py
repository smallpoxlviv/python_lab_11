import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../model')

from abstract_dwelling import AbstractDwelling
from city_infrastructure import CityInfrastructure

class DwellingManager:
    def __init__(self, dwellings = []):
        self.dwellings = dwellings
    
    def add_dwelling(self, dwelling):
        self.dwellings.append(dwelling)

    def form_propositions(self):
        return self.dwellings

    def form_propositions_by_distance_in_meters_to_all_buildings_of_infrastructure\
        (self, distance_in_meters, city):
        new_list_of_dwellings = []
        for dwelling in self.dwellings:
            if dwelling.calculate_distance_to_closer_school_in_meters(city.locations_of_schools) < distance_in_meters\
            and dwelling.calculate_distance_to_closer_kindergarden_in_meters(city.locations_of_kindergardens) < distance_in_meters\
            and dwelling.calculate_distance_to_closer_playground_in_meters(city.locations_of_playgrounds) < distance_in_meters:
                new_list_of_dwellings.append(dwelling)
        return new_list_of_dwellings        