from flask import Flask, render_template, request, session, send_file
from api.weather_api import (
    get_geocode_by_city_name,
    get_weather_on_location,
    load_api_key_from_env,
    get_weather_5_days,
)
from graphs.generate_plotlib import plot_daily_weather
from data.data_processing import calculate_daily_averages

import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_weather", methods=["POST"])
def get_weather():
    city_name = request.form["city"]
    api_key = load_api_key_from_env()
    lat, lon = get_geocode_by_city_name(city_name, api_key)
    if lat is not None and lon is not None:
        weather_data = get_weather_on_location(lat, lon, api_key)
        session["weather_data"] = weather_data
        return render_template("weather_result.html", weather=weather_data)
    else:
        return "Falha ao obter dados da cidade."


@app.route("/next_5_days", methods=["GET"])
def next_day():
    weather_data = session.get("weather_data")
    if weather_data:
        api_key = load_api_key_from_env()
        weather_5_days = get_weather_5_days(
            weather_data["coord"]["lat"], weather_data["coord"]["lon"], api_key
        )
        weather_5_days = calculate_daily_averages(weather_5_days)
        if weather_5_days:
            session["five_days"] = weather_5_days
            return render_template("next_5_days.html", weather=weather_5_days)
        else:
            return "Failed to fetch weather data for the next 5 days."
    else:
        return "Weather data not found in session."


@app.route("/weather_plot.png")
def weather_plot():
    daily_stats = session.get("five_days")
    if not daily_stats:
        return "Data not found", 404
    buf = plot_daily_weather(daily_stats)
    return send_file(buf, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
