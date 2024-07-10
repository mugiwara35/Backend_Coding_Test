from sqlalchemy import Table, Column, DateTime, Integer, String, Float, Boolean, SmallInteger, DateTime, Numeric, BigInteger, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime

Base  = declarative_base()
    
# END::TABEL ASSOCIATION

class EMPLOYEE(Base):
    __tablename__ = 'employee'

    id = Column(BigInteger, primary_key=True, index=True)
    
    name = Column(String)
    phone = Column(String)
    wages = Column(Numeric(12, 2), default=0)
    role = Column(String)
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())