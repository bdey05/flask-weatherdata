from flask import Flask
from config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    
    from dashboard.main import bp as dashboardbp
    app.register_blueprint(dashboardbp)
    
    from dashboard.dbload import bp as dbloadbp
    app.register_blueprint(dbloadbp)

    return app 
