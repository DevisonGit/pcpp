import xml.etree.ElementTree as ET


class TemperatureConverter:
    @staticmethod
    def convert_celsius_to_fahrenheit(celsius):
        return 9 / 5 * float(celsius) + 32


class ForecastXmlParser:
    def __init__(self):
        self.tree = ET.parse('forecast.xml')
        self.root = self.tree.getroot()
        self.temperature = TemperatureConverter()

    def parse(self):
        for item in self.root.findall('item'):
            day = item[0].text
            celsius = item[1].text
            fahrenheit = self.temperature.convert_celsius_to_fahrenheit(celsius)
            print(f'{day}: {celsius} Celsius, {fahrenheit:.1f} Fahrenheit')


app = ForecastXmlParser()
app.parse()
