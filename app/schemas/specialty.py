from typing import Dict, Any, Optional, Type, List
from pydantic import BaseModel


class Specialty(BaseModel):

    code: str
    title: str
    description: str

class SpecialtyCreate(Specialty):
    pass

class SpecialtyUpdate(Specialty):
    code: Optional[str]
    title: Optional[str]
    description: Optional[str]