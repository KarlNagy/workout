from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists,create_database
import yaml

secrets = yaml.safe_load(open('secrets.yaml'))
engine = create_engine(secrets['database_URI'])

if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))