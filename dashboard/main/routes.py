from dashboard.main import bp
from flask import render_template
from dashboard.weather import GetWeatherStats

@bp.route('/')
@bp.route('/dashboard/')
def dashboard():
    df = GetWeatherStats()
    return render_template('main/main.html', df=df)
     