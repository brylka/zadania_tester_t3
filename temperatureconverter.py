class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32
    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9
    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15
    def kelvin_to_celsius(self,kelvin):
        return kelvin - 273.15
    def fahrenheit_to_kelvin(self,fahrenheit):
        return (fahrenheit + 459.67) * 5 / 9
    def kelvin_to_fahrenheit(self, kelvin):
        return kelvin * 9 / 5 - 459.67