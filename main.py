from api.weather_api import (
    get_geocode_by_city_name,
    get_weather_on_location,
    load_api_key_from_env,
    get_weather_5_days
)
from data.data_processing import calculate_daily_averages
from graphs.generate_plotlib import plot_daily_weather

api_key = load_api_key_from_env()


def main():
    city_name = "Franco da Rocha"
    lat, lon = get_geocode_by_city_name(city_name, api_key)

    if lat is not None and lon is not None:
        get_weather_on_location(lat, lon, api_key)
        weather_data = get_weather_5_days(lat, lon, api_key)
        daily_averages = calculate_daily_averages(weather_data)
        print(plot_daily_weather(daily_averages))


if __name__ == "__main__":
    main()
