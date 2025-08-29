import api_schemas
from database import get_db, SessionLocal
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import models

router = APIRouter()

@router.get("/customer/{customer_id}", response_model=api_schemas.CustomerResponse, status_code=status.HTTP_200_OK)
def get_customer(customer_id: str, db: Session = Depends(get_db)):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.get("/customers", response_model=List[api_schemas.CustomerResponse], status_code=status.HTTP_200_OK)
def get_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = db.query(models.Customer).offset(skip).limit(limit).all()
    if not customers:
        raise HTTPException(status_code=404, detail="No customers found")
    return customers    

@router.post("/makecustomer", response_model=api_schemas.CustomerResponse, status_code=status.HTTP_201_CREATED)
def create_customer(customer: api_schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.email == customer.email).first()
    if db_customer:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_customer = models.Customer(
        name=customer.name,
        email=customer.email,
        city=customer.city,
        state=customer.state,
        country=customer.country,
        phone=customer.phone,
        description=customer.description,
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# Update Customer
@router.put("/updatecustomer/{customer_id}", response_model=api_schemas.CustomerResponse, status_code=status.HTTP_200_OK)
def update_customer(customer_id: str, customer: api_schemas.CustomerUpdate, db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    for var, value in vars(customer).items():
        if value is not None:
            setattr(db_customer, var, value)
    
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer
