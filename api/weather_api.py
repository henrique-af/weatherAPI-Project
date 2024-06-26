import requests


# Load API Key
def load_api_key_from_env(file_path=".env"):
    with open(file_path, "r") as file:
        for line in file:
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split("=", 1)
                if key.strip() == "API_KEY_WEATHER":
                    return value.strip()
    return None


# Getting the latitude/longitude values
def get_geocode_by_city_name(city, api_weather):
    request_url = (
        f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_weather}"
    )
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])
        return lat, lon
    else:
        return None


# Getting data
def get_weather_on_location(lat, lon, api_weather):

    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_weather}&units=metric&lang=pt_br"
    )
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

# 5 days of weather
def get_weather_5_days(lat, lon, api_weather):
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_weather}&units=metric"
        )

        if response.status_code == 200:
            weather_data = response.json()
            return weather_data
        else:
            print(f"Error: Received status code {response.status_code} from API")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
