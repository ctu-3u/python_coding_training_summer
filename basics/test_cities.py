import unittest

from city_country import city_country as ccpair

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        get_ccpair = ccpair('lausanne','switzerland')
        self.assertEqual(get_ccpair,"Lausanne, Switzerland")

    def test_city_country_site(self):
        get_ccs = ccpair('lausanne','switzerland','lac lemon')
        self.assertEqual(get_ccs,"Lausanne, Switzerland - famous sites: Lac Lemon")


unittest.main()