import api_schemas
from database import get_db,session
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import models

router = APIRouter()



@router.get("/tenant/{tenant_id}",reponse_model=api_schemas.TenantResponse,status_code=status.HTTP_200_OK)
def get_tenant(tenant_id: str, db : Session = Depends(get_db)):
    # Logic to retrieve a tenant by ID
    tenant = db.query(models.Tenant).filter(models.Tenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant

@router.get("/tenants",response_model=List[api_schemas.TenantResponse],status_code=status.HTTP_200_OK)
def get_tenants(skip: int = 0 , limit : int = 100,db: Session = Depends(get_db)):
    # Logic to retrieve all tenants
    tenants = db.query(models.Tenant).offset(skip).limit(limit).all()
    if not tenants:
        raise HTTPException(status_code=404, detail="No tenants found")
    return tenants

@router.post("/maketenant",response_model=api_schemas.TenantCreate,status_code=status.HTTP_201_CREATED)
def create_tenant(tenant: api_schemas.TenantCreate, db: Session = Depends(get_db)):
    db_tenant = db.query(models.Tenant).filter(models.Tenant.email == tenant.email).first()
    if db_tenant:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    #Create a new tenant if email is not registered
    db_tenant = models.Tenant(
        name = tenant.name,
        email = tenant.email,
        country = tenant.country,
        currency = tenant.currency,
        tax_id = tenant.tax_id,
        
    )
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    return db_tenant
