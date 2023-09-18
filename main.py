from scrape import WeatherFinder

import sys


if __name__ == "__main__":
    print(f"In {sys.argv[1]}, {WeatherFinder(sys.argv[1]).makeWeather()}")