if __name__ == "__main__":
    import sys, os
    myPath = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, myPath + '/../../main/model')
    sys.path.insert(0, myPath + '/../../main/manager')

    import doctest 
    from dwelling_manager import DwellingManager
    from city_infrastructure import CityInfrastructure
    from base_dwelling_manager_test import *

    dwelling_manager = DwellingManager()
    fill_dwelling_manager(dwelling_manager)

    city = CityInfrastructure()
    add_infrastructure(city)

    def test_forming_propositions_by_distance_in_meters_to_all_buildings_of_Infrastructure():
        """
        >>> acceptable_dwellings = dwelling_manager.form_propositions_by_distance_in_meters_to_all_buildings_of_infrastructure(2000, city)
        >>> print(acceptable_dwellings[0].location.x_in_decimal_degrees)
        49.838883
        >>> print(acceptable_dwellings[1].location.x_in_decimal_degrees)
        49.846594
        """
    def test_fotming_propositions():
        """
        >>> acceptable_dwellings = dwelling_manager.form_propositions()
        >>> print(acceptable_dwellings[0].location.x_in_decimal_degrees)
        49.838883
        >>> print(acceptable_dwellings[1].location.x_in_decimal_degrees)
        49.825672
        >>> print(acceptable_dwellings[2].location.x_in_decimal_degrees)
        49.846594
        >>> print(acceptable_dwellings[3].location.x_in_decimal_degrees)
        49.765081
        >>> print(acceptable_dwellings[0].location.y_in_decimal_degrees)
        24.027453
        >>> print(acceptable_dwellings[1].location.y_in_decimal_degrees)
        23.954481
        >>> print(acceptable_dwellings[2].location.y_in_decimal_degrees)
        24.025002
        >>> print(acceptable_dwellings[3].location.y_in_decimal_degrees)
        23.842558
        """
    doctest.testmod()