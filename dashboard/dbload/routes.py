from dashboard.dbload import bp 
from flask import render_template 
from ..weather import GetWeatherStats 
from dashboard.models.weathermodel import WeatherModel  
from dashboard import db

@bp.route('/dbload')
def load():
    data = GetWeatherStats()
    for index, row in data.iterrows():
        daily_weather_report = WeatherModel(time=row['Time'], 
                                            max_temp=row['Max Temperature'],
                                            min_temp=row['Min Temperature'],
                                            app_max_temp=row['Apparent Max Temperature'],
                                            app_min_temp=row['Apparent Min Temperature']) 
    db.session.add(daily_weather_report)
    db.session.commit()
    return render_template('dbload/dbload.html')