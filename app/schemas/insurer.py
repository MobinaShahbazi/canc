from typing import Dict, Any, Optional, Type, List
from pydantic import BaseModel


class Insurer(BaseModel):

    code: str
    name: str

class InsurerCreate(Insurer):
    pass

class InsurerUpdate(BaseModel):
    pass