from temperatureconverter import TemperatureConverter
import unittest

class TestTemperatureConverter(unittest.TestCase):
    def setUp(self):
        self.converter = TemperatureConverter()
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(32, self.converter.celsius_to_fahrenheit(0))
        self.assertEqual(212, self.converter.celsius_to_fahrenheit(100))
    def test_fahrenheit_to_celsius(self):
        self.assertEqual(0, self.converter.fahrenheit_to_celsius(32))
        self.assertEqual(100, self.converter.fahrenheit_to_celsius(212))
    def test_celsius_to_kelvin(self):
        self.assertEqual(0, self.converter.celsius_to_kelvin(-273.15))
    def test_kelvin_to_celsius(self):
        self.assertEqual(-273.15, self.converter.kelvin_to_celsius(0))
    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(310.93, self.converter.fahrenheit_to_kelvin(100), places=2)
    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(100, self.converter.kelvin_to_fahrenheit(310.93), places=2)
