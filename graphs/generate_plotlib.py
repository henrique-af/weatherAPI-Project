import matplotlib.pyplot as plt
from io import BytesIO


def plot_daily_weather(daily_stats):
    dates = []
    min_temperatures = []
    max_temperatures = []
    avg_temperatures = []
    avg_humidities = []
    rainy_days = []
    severe_weather_days = []

    for date, stats in daily_stats.items():
        dates.append(date)
        city = stats["city"]
        min_temperatures.append(stats["min_temperature"])
        max_temperatures.append(stats["max_temperature"])
        avg_temperatures.append(stats["average_temperature"])
        avg_humidities.append(stats["average_humidity"])
        rainy_days.append(stats["rainy_days"])
        severe_weather_days.append(stats["severe_weather_days"])

    plt.figure(figsize=(12, 6))

    plt.plot(
        dates, min_temperatures, marker="o", color="#1f77b4", label="Temperatura mínima"
    )
    plt.plot(
        dates, max_temperatures, marker="o", color="#ff7f0e", label="Temperatura máxima"
    )
    plt.plot(
        dates,
        avg_temperatures,
        linestyle="--",
        marker="o",
        color="#2ca02c",
        label="Temperatura média",
    )

    rainy_dates = [dates[i] for i, rainy_day in enumerate(rainy_days) if rainy_day > 0]
    rainy_temperatures = [
        min_temperatures[i] for i, rainy_day in enumerate(rainy_days) if rainy_day > 0
    ]
    plt.scatter(
        rainy_dates,
        rainy_temperatures,
        color="#d62728",
        label="Dia de chuva" if rainy_dates else None,
        zorder=5,
    )

    severe_dates = [
        dates[i] for i, severe_day in enumerate(severe_weather_days) if severe_day > 0
    ]
    severe_temperatures = [
        max_temperatures[i]
        for i, severe_day in enumerate(severe_weather_days)
        if severe_day > 0
    ]
    plt.scatter(
        severe_dates,
        severe_temperatures,
        color="#9467bd",
        label="Risco de chuva severa" if severe_dates else None,
        zorder=5,
    )

    print(city)

    plt.xlabel("Data")
    plt.ylabel("Valores em ºC")
    plt.title(f"Previsão de 5 dias em {city}")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return buf
