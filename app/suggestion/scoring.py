import haversine as hs
from haversine import Unit
from sqlalchemy.orm import Session
from app.crud import doctor_crud
from app.crud.base import CRUDBase
from app.dependencies import get_db
from app.models import Doctor
from app.schemas import Doctor


def distance(loc, province, specialty):  # patient insurance add

    res = get_db()
    db = next(res)

    filtered_doctors = doctor_crud.filter_by(db, name="naghme", limit=10)

    # Print out the filtered doctors
    for doctor in filtered_doctors:
        print(doctor.name)

distance(1,"Tehran",2)
