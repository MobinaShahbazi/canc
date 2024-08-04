from typing import Dict, Any, Optional, Type, List
from pydantic import BaseModel


class Doctor(BaseModel):

    name: str
    lastname: str
    code: str
    description: str
    specialty_id: int

class DoctorCreate(Doctor):
    pass

class DoctorCreateBulk(BaseModel):

    values: List[DoctorCreate]

class DoctorUpdate(Doctor):

    name: Optional[str]
    lastname: Optional[str]
    code: Optional[str]
    description: Optional[str]
    specialty_id: Optional[int] 

