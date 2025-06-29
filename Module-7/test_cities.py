# Joel Atkinson Assignment 7.2 Test Cities File Advanced Python CSD-325

import unittest
import city_functions

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        city = 'Vancouver'
        country = 'Canada'
        result = city_functions.city_country(city, country)
        expected = city + ', ' + country
        self.assertEqual(result, expected)
        print('Test passed')
        print('Expecting: ' + expected)
        print('Returned: ' + result)


if __name__ == '__main__':
    unittest.main()