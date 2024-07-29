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
    db_name: str = 'app_db'
    sqlalchemy_database_url: str = f'mysql+pymysql://root:1211381msh@127.0.0.1:3306/{db_name}'
    # jdbc:mysql://localhost:3306
    # mysql://root:1211381msh@localhost:3306


app_config = CommonSettings()
