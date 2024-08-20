from typing import Dict, Any, Optional, Type, List
from pydantic import BaseModel

class MedicalCenter(BaseModel):

    title: str
    province: str
    city: str
    address: str
    latitude: str
    longitude: str
    phone: str
    specialties: Optional[List[str]]
    services: Optional[List[str]]
    doctor_id: str             # -> int

class MedicalCenterCreate(MedicalCenter):
    pass

class MedicalCenterUpdete(MedicalCenter):
    title: Optional[str]
    province: Optional[str]
    city: Optional[str]
    address: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    phone: Optional[str]
    specialties: Optional[List[str]]
    services: Optional[List[str]]
    doctor_id: Optional[List[str]]  # -> int
