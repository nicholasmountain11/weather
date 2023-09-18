from requests_html import HTMLSession
from weather import Weather

s = HTMLSession()

class WeatherFinder:

    r: str

    def __init__(self, location: str) -> None:
        url = f'https://www.google.com/search?q=weather+{location}'
        self.r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})


    def makeWeather(self) -> Weather:
        return Weather(self.r.html.find('span#wob_tm', first=True).text, self.r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text, self.r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text)
