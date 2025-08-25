from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class MyConfig:
    max_anystr_length = 10
    validate_assignment = True
    error_msg_templates = {
        'value_error.any_str.max_length': 'max_length:{limit_value}',
    }
# Tenant schema
class TenantBase(BaseModel):
    name: str
    email: str
    country: str = "India"  # Added default value
    currency: str = "INR"   # Added default value
    tax_id: Optional[str] = None

class TenantCreate(TenantBase):
    pass

class TenantResponse(TenantBase):
    id: str  # Changed from int to str since you're using UUID

    class Config:
        from_attributes = True  # Fixed the typo


#Plan Schema
class PlanBase(BaseModel):
    name : str
    description : Optional[str] = None
    amount : str
    currency : str = "INR"
    interval : str  # e.g., 'month', 'year'
    
class PlanCreate(PlanBase):
    pass

class PlanResponse(PlanBase):
    id : int
    is_active : str
    
    class Config:
        from_attribute = True
        
#Customer Schema
class CustomerBase(BaseModel):
    name : str
    email : str
    city : Optional[str] = None
    state : Optional[str] = None
    country : Optional[str] = None
    phone : Optional[str] = None
    description : Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id : str

    class Config:
        from_attribute = True
        

#1. TenantBase - The Foundation
# Purpose: Defines the common fields that ALL tenant-related schemas will have.

# Key characteristics:

# name: str - Required string field

# email: EmailStr - Required email field (Pydantic validates email format)

# country: str = "India" - String with default value "India"

# currency: str = "INR" - String with default value "INR" (Indian Rupee)

# tax_id: Optional[str] = None - Optional field that can be None

# Use case: Serves as a base for other tenant schemas to avoid code duplication
        
#2. TenantCreate - For Creating New Tenants
# Purpose: Used when creating a new tenant.
# Inherits from TenantBase, so it has all the same fields.
# Key characteristics: No additional fields; just inherits everything from TenantBase.
# Use case: When a new tenant is being created, this schema ensures all required fields are provided.

#3. TenantResponse - For API Responses(Must be Strict)
# Purpose: Used when sending tenant data back in API responses.
# Inherits from TenantBase, so it has all the same fields.
# Key characteristics:
# id: int - Unique identifier for the tenant
# is_active: bool - Indicates if the tenant is active
# created_at: datetime - Timestamp of when the tenant was created
# class Config:
# from_attributes = True - Allows compatibility with ORM models
# Use case: When returning tenant data from the API, this schema includes additional metadata fields.
