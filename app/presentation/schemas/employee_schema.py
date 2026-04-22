from pydantic import BaseModel
from typing import Optional


class EmployeeCreate(BaseModel):
    name: str
    email: str
    phone_number: str
    position: str
    
class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    position: Optional[str] = None

class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    phone_number: str
    position: str