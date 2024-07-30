from pydantic import PostgresDsn
from pydantic_settings import BaseSettings

class CommonSettings(BaseSettings):

    # Basic application configs
    app_port: int = 42420

    # General application configs
    app_name: str = 'Development'
    app_version: str = '0.0.1'

    # TODO Can use PostgresDsn data type here but results in an error
    # SWH Database Configs
    db_name: str = 'postgres'
    # sqlalchemy_database_url: str = f'mysql+pymysql://root:1211381msh@127.0.0.1:3306/{db_name}'
    sqlalchemy_database_url: str = f'postgresql+psycopg2://postgres:1211381msh@127.0.0.1:5432/{db_name}'



app_config = CommonSettings()
