from .session import SessionLocal, db_engine
from .base_class import Base
from .init_db import init_Speciaity
from .init_db import init_Insurer
from .init_db import init_Doctor
from .init_db import init_Medical_Center

# Initialize application database
Base.metadata.create_all(bind=db_engine)
