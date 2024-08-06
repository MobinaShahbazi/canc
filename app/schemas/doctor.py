from typing import Dict, Any, Optional, Type, List
from pydantic import BaseModel


class Doctor(BaseModel):

    name: str
    lastname: str
    nezamCode: str
    gender: str
    rate: float
    specialty_code: str

class DoctorCreate(Doctor):
    pass

class DoctorCreateBulk(BaseModel):

    values: List[DoctorCreate]

class DoctorUpdate(Doctor):

    name: Optional[str]
    lastname: Optional[str]
    nezamCode: Optional[str]
    gender: Optional[str]
    rate: Optional[float]
    specialty_code: Optional[str]

