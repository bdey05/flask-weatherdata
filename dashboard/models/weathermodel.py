from dashboard import db
from sqlalchemy import Date, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column
import datetime 

class WeatherModel(db.Model):
    time: Mapped[datetime.date] = mapped_column(Date, primary_key=True)
    max_temp: Mapped[float] = mapped_column(Float, nullable=False)
    min_temp: Mapped[float] = mapped_column(Float, nullable=False)
    app_max_temp: Mapped[float] = mapped_column(Float, nullable=False)
    app_min_temp: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'Weather on {self.time}'
    
    def to_dict(self):
        return {
            'time': self.time,
            'max_temp': self.max_temp,
            'min_temp': self.min_temp,
            'app_max_temp': self.app_max_temp,
            'app_min_temp': self.app_min_temp
        }


