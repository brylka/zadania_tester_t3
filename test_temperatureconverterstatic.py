from temperatureconverterstatic import TemperatureConverter
import unittest

class TestTemperatureConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(32, TemperatureConverter.celsius_to_fahrenheit(0))
        self.assertEqual(212, TemperatureConverter.celsius_to_fahrenheit(100))
    def test_fahrenheit_to_celsius(self):
        self.assertEqual(0, TemperatureConverter.fahrenheit_to_celsius(32))
        self.assertEqual(100, TemperatureConverter.fahrenheit_to_celsius(212))
    def test_celsius_to_kelvin(self):
        self.assertEqual(0, TemperatureConverter.celsius_to_kelvin(-273.15))
    def test_kelvin_to_celsius(self):
        self.assertEqual(-273.15, TemperatureConverter.kelvin_to_celsius(0))
    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(310.93, TemperatureConverter.fahrenheit_to_kelvin(100), places=2)
    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(100, TemperatureConverter.kelvin_to_fahrenheit(310.93), places=2)

if __name__ == '__main__':
    unittest.main()