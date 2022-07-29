from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import yaml

app = Flask(__name__)

secret = yaml.safe_load(open('secrets.yaml'))

app.config['SECRET_KEY'] = secret['secret_key']
app.config['SQLALCHEMY_DATABASE_URI'] = secret['database_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)




from myproject.sessions.views import sessions_blueprint


app.register_blueprint(sessions_blueprint,url_prefix='/sessions')