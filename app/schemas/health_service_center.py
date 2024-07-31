from typing import Dict, Any, Optional, Type, List
from pydantic import BaseModel

class HelthServiceCenter(BaseModel):

    title: str
    province: str
    district: str
    city: str
    address: str
    latitude: str
    longitude: str
    phone: str
    specialties: Optional[List[str]]
    services: Optional[List[str]]
    doctor_id: int

class HelthServiceCenterCreate(HelthServiceCenter):
    pass

class HelthServiceCenterUpdete(HelthServiceCenter):
    title: Optional[str] = None
    province: Optional[str] = None
    district: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    phone: Optional[str] = None
    specialties: Optional[List[str]] = None
    services: Optional[List[str]] = None
    doctor_id: Optional[List[int]] = None
