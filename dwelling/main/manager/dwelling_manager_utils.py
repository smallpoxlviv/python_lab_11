import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../model')

from abstract_dwelling import AbstractDwelling
from sort_type import SortType
#from city_infrastructure import CityInfrastructure
class DwellingManagerUtils:
    @staticmethod
    def area_sorter(dwelling):
        return dwelling.area_in_square_meters

    @staticmethod
    def sort_by_area(dwellings, sort_type):
        dwellings.sort(key = DwellingManagerUtils.area_sorter,\
            reverse = True if sort_type == SortType.DESC else False)

    @staticmethod
    def price_sorter(dwelling):
        return dwelling.price_in_USD

    @staticmethod
    def sort_by_price(dwellings, sort_type):
        dwellings.sort(key = DwellingManagerUtils.price_sorter,\
            reverse = True if sort_type == SortType.DESC else False)

    @staticmethod
    def sort_by_price_and_area(dwellings, sort_type):
        dwellings.sort(key = DwellingManagerUtils.area_sorter,\
            reverse = True if sort_type == SortType.DESC else False)
        dwellings.sort(key = DwellingManagerUtils.price_sorter,\
            reverse = True if sort_type == SortType.DESC else False)

    @staticmethod
    def district_sorter(dwelling):
        return dwelling.district

    @staticmethod
    def sort_by_district(dwellings, sort_type):
        dwellings.sort(key = DwellingManagerUtils.district_sorter,\
            reverse = True if sort_type == SortType.DESC else False)
        