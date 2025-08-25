from sqlalchemy import Column, String
import uuid
from database import Base

class Tenant(Base):
    __tablename__ = "tenants"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    country = Column(String)
    currency = Column(String)
    tax_id = Column(String)
    class Config:
        from_attributes = True
        orm_mode = True

class Plan(Base):
    __tablename__ = "plans"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=True)
    description = Column(String, nullable=False)
    amount = Column(String, nullable=False)
    currency = Column(String, nullable=False)
    interval = Column(String, nullable=False)  # e.g., 'month', 'year'
    is_active = Column(String, default=True)
    
    class Config:
        from_attributes = True
        orm_mode = True
        
class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    country = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    description = Column(String, nullable=True)
    
    class Config:
        from_attributes = True
        orm_mode = True