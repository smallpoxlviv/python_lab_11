import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../main/model')

from mansion import Mansion
from location import Location
from city_infrastructure import CityInfrastructure

def create_mansions():
    dwellings = [
        Mansion(45.2, 55000, Location(49.838883, 24.027453), "Syhivski", 0),
        Mansion(18.5, 46000, Location(49.825672, 23.954481), "Frankivski", 2),
        Mansion(108.3, 51000, Location(49.846594, 24.025002), "Shevchenkivski", 1),
        Mansion(100, 55000, Location(49.765081, 23.842558), "Zaliznychni", 1)
    ]
    return dwellings

def add_infrastructure(city_infrastructure):
    city_infrastructure.add_school(49.841863, 24.029012)
    city_infrastructure.add_school(49.845661, 24.034215)
    city_infrastructure.add_kindergarden(49.839290, 24.017122)
    city_infrastructure.add_kindergarden(49.843367, 24.009523)
    city_infrastructure.add_playground(49.843816, 24.035229)
    city_infrastructure.add_playground(49.839023, 24.019074)

def fill_dwelling_manager(dwelling_manager):
    dwelling_manager.add_dwelling(Mansion(45.2, 52000, Location(49.838883, 24.027453), "Syhivski", 0))
    dwelling_manager.add_dwelling(Mansion(18.5, 46000, Location(49.825672, 23.954481), "Frankivski", 2))
    dwelling_manager.add_dwelling(Mansion(108.3, 51000, Location(49.846594, 24.025002), "Shevchenkivski", 1))
    dwelling_manager.add_dwelling(Mansion(100, 55000, Location(49.765081, 23.842558), "Zaliznychni", 1))