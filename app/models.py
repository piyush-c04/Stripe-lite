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