if __name__ == "__main__":
    import sys, os
    myPath = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, myPath + '/../../main/model')
    sys.path.insert(0, myPath + '/../../main/manager')

    import doctest
    from dwelling_manager_utils import DwellingManagerUtils
    from sort_type import SortType
    from base_dwelling_manager_test import create_mansions

    dwellings = create_mansions()

    def test_sorting_descending_by_area():
        """
        >>> DwellingManagerUtils.sort_by_area(dwellings, SortType.DESC)
        >>> print(dwellings[0].area_in_square_meters)
        108.3
        >>> print(dwellings[1].area_in_square_meters)
        100
        >>> print(dwellings[2].area_in_square_meters)
        45.2
        >>> print(dwellings[3].area_in_square_meters)
        18.5
        """

    def test_sorting_ascending_by_area():
        """
        >>> DwellingManagerUtils.sort_by_area(dwellings, SortType.ASC)
        >>> print(dwellings[0].area_in_square_meters)
        18.5
        >>> print(dwellings[1].area_in_square_meters)
        45.2
        >>> print(dwellings[2].area_in_square_meters)
        100
        >>> print(dwellings[3].area_in_square_meters)
        108.3
        """

    def test_sorting_descending_by_price():
        """
        >>> DwellingManagerUtils.sort_by_price(dwellings, SortType.DESC)
        >>> print(dwellings[0].price_in_USD)
        55000
        >>> print(dwellings[1].price_in_USD)
        55000
        >>> print(dwellings[2].price_in_USD)
        51000
        >>> print(dwellings[3].price_in_USD)
        46000
        """

    def test_sorting_ascending_by_price():
        """
        >>> DwellingManagerUtils.sort_by_price(dwellings, SortType.ASC)
        >>> print(dwellings[0].price_in_USD)
        46000
        >>> print(dwellings[1].price_in_USD)
        51000
        >>> print(dwellings[2].price_in_USD)
        55000
        >>> print(dwellings[3].price_in_USD)
        55000
        """

    def test_sorting_descending_by_price_and_area():
        """
        >>> DwellingManagerUtils.sort_by_price_and_area(dwellings, SortType.DESC)
        >>> print(dwellings[0].price_in_USD)
        55000
        >>> print(dwellings[1].price_in_USD)
        55000
        >>> print(dwellings[2].price_in_USD)
        51000
        >>> print(dwellings[3].price_in_USD)
        46000
        >>> print(dwellings[0].area_in_square_meters)
        100
        >>> print(dwellings[1].area_in_square_meters)
        45.2
        """

    def test_sorting_ascending_by_price_and_area():
        """
        >>> DwellingManagerUtils.sort_by_price_and_area(dwellings, SortType.ASC)
        >>> print(dwellings[0].price_in_USD)
        46000
        >>> print(dwellings[1].price_in_USD)
        51000
        >>> print(dwellings[2].price_in_USD)
        55000
        >>> print(dwellings[3].price_in_USD)
        55000
        >>> print(dwellings[2].area_in_square_meters)
        45.2
        >>> print(dwellings[3].area_in_square_meters)
        100
        """

    def test_sorting_descending_by_district():
        """
        >>> DwellingManagerUtils.sort_by_district(dwellings, SortType.DESC)
        >>> print(dwellings[0].district)
        Zaliznychni
        >>> print(dwellings[1].district)
        Syhivski
        >>> print(dwellings[2].district)
        Shevchenkivski
        >>> print(dwellings[3].district)
        Frankivski
        """

    def test_sorting_ascending_by_district():
        """
        >>> DwellingManagerUtils.sort_by_district(dwellings, SortType.ASC)
        >>> print(dwellings[0].district)
        Frankivski
        >>> print(dwellings[1].district)
        Shevchenkivski
        >>> print(dwellings[2].district)
        Syhivski
        >>> print(dwellings[3].district)
        Zaliznychni
        """
    doctest.testmod()