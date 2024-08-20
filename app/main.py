import uvicorn
from fastapi import FastAPI
from app.config import app_config
from app.db import db_engine
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

# import api endpoint here
from app.api import AppInfo, DoctorDAO, MedicalCenterDAO, OtherDAO

# Initialize the application
app = FastAPI()

# Set templating preferences
script_dir = os.path.dirname(__file__)
app.mount('/static', StaticFiles(directory=os.path.join(script_dir, "static/")), name='static')
# templates = Jinja2Templates(directory='templates/')

# Define some common endpoints for all services
app.include_router(AppInfo().router)

# Add API routes here
app.include_router(OtherDAO().router)
app.include_router(DoctorDAO().router)
app.include_router(MedicalCenterDAO().router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=app_config.app_port)
