from typing import Dict, Any, Optional, Type, List
from pydantic import BaseModel


class Doctor(BaseModel):

    name: str
    lastname: str
    specialization: str
    code: str
    description: str 
    address: str
    phone: str

class DoctorCreate(Doctor):
    pass

class DoctorCreateBulk(BaseModel):

    values: List[DoctorCreate]

class DoctorUpdate(Doctor):

    name: Optional[str] = None
    lastname: Optional[str] = None
    specialization: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None 
    address: Optional[str] = None
    phone: Optional[str] = None

