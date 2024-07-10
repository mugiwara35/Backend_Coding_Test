from pydantic import BaseModel
from decimal import Decimal
from typing import Optional

class Employee_SchemaCreate(BaseModel):
    name: str
    phone: str
    wages: Decimal
    role: str
    
    class Config:
        from_attributes = True
        
class Employee_SchemaUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    phone: Optional[str] = None
    wages: Optional[Decimal] = 0
    role: Optional[str] = None
    
    class Config:
        from_attributes = True
        
class Employee_SchemaId(BaseModel):
    id: int
    
    class Config:
        from_attributes = True