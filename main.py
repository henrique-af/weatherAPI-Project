import requests
import pandas as pd
import os


data = get_geocode_by_city_name("Franco da Rocha")
print(get_weather_on_location(data))
