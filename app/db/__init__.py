from .session import SessionLocal, db_engine
from .base_class import Base
from .init_db import init_speciaity
from .init_db import init_insurer

# Initialize application database
Base.metadata.create_all(bind=db_engine)
