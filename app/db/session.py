from app.config import app_config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_engine = create_engine(app_config.sqlalchemy_database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)