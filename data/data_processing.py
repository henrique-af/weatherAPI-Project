from collections import defaultdict


def calculate_daily_averages(weather_data):
    
    daily_averages = defaultdict(list)

    for item in weather_data["list"]:
        date = item["dt_txt"].split()[0]
        city = weather_data["city"]["name"]
        daily_averages[date].append(item)

    daily_stats = {}
    for date, data in daily_averages.items():
        temperatures = [item.get("main", {}).get("temp", 0) for item in data]
        humidity = [item.get("main", {}).get("humidity", 0) for item in data]
        temp_min = [item.get("main", {}).get("temp_min", 0) for item in data]
        temp_max = [item.get("main", {}).get("temp_max", 0) for item in data]
        rainy_days = sum(1 for item in data if "rain" in item)
        severe_weather_days = sum(
            1 for item in data if "storm" in item or "rain" in item
        )

        daily_stats[date] = {
            "date": date,
            "city": city,
            "average_temperature": (
                sum(temperatures) / len(temperatures) if temperatures else 0
            ),
            "average_humidity": sum(humidity) / len(humidity) if humidity else 0,
            "min_temperature": min(temp_min) if temp_min else 0,
            "max_temperature": max(temp_max) if temp_max else 0,
            "rainy_days": rainy_days,
            "severe_weather_days": severe_weather_days,
        }

    return daily_stats
