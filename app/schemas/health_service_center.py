from typing import Dict, Any, Optional, Type, List
from pydantic import BaseModel

class Center(BaseModel):

    title: str
    province: str
    district: str
    city: str
    address: str
    phone: str
    specialties: List[str]
    services: List[str]

class CenterCreate(Center):
    pass

class CenterUpdete(Center):
    title: Optional[str] = None
    province: Optional[str] = None
    district: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    specialties: Optional[List[str]] = None
    services: Optional[List[str]] = None
