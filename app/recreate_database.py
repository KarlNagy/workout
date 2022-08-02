from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists,create_database
import yaml

secrets = yaml.safe_load(open('secrets.yaml'))
engine = create_engine(secrets['database_URI'])



if database_exists(engine.url):
    connection = engine.connect()
    connection.execute(text("DROP DATABASE IF EXISTS workout;"))
    create_database(engine.url)


print(database_exists(engine.url))