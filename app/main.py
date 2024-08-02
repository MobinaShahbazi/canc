import uvicorn
from fastapi import FastAPI
from app.config import app_config
from app.db import db_engine
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# import api endpoint here
from app.api import AppInfo, DoctorDAO, MedicalCenterDAO

# Initialize the application
app = FastAPI()

# Set templating preferences
app.mount('/app/static', StaticFiles(directory='static'), name='static')
# templates = Jinja2Templates(directory='templates/')

# Define some common endpoints for all services
app.include_router(AppInfo().router)

# Add API routes here
app.include_router(DoctorDAO().router)
app.include_router(MedicalCenterDAO().router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=app_config.app_port)
