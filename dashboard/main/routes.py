from dashboard.main import bp
import requests 
from config import Config
import pandas as pd
from flask import render_template

def GetWeatherStats():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 40.8701,
        "longitude": -73.8857,
        "daily": ["temperature_2m_max", "temperature_2m_min", "apparent_temperature_max", "apparent_temperature_min", "sunrise", "sunset", "daylight_duration", "sunshine_duration", "uv_index_max", "precipitation_sum", "precipitation_hours", "precipitation_probability_max", "wind_speed_10m_max", "wind_direction_10m_dominant"],
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
        "timezone": "America/New_York",
        "past_days": 92
    }
    data = requests.get(url, params=params).json()
    df = pd.DataFrame(data['daily']).iloc[:, :5]
    newcolumns = {
        'time': 'Time', 
        'temperature_2m_max': 'Max Temperature', 
        'temperature_2m_min': 'Min Temperature', 
        'apparent_temperature_max': 'Apparent Max Temperature', 
        'apparent_temperature_min': 'Apparent Min Temperature'
    }
    df.rename(columns=newcolumns, inplace=True)
    df.reset_index()
    df.dropna(inplace=True)
   
    return df

@bp.route('/')
@bp.route('/dashboard/')
def dashboard():
    df = GetWeatherStats()
    return render_template('main/main.html', df=df)
     