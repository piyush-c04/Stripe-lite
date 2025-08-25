from tkinter import SE
import api_schemas
from database import get_db, SessionLocal
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import models

router = APIRouter()

@router.get("/plan/{plan_id}", response_model=api_schemas.PlanResponse, status_code=status.HTTP_200_OK)
def get_plan(plan_id: str, db: Session = Depends(get_db)):
    plan = db.query(models.Plan).filter(models.Plan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

@router.get("/plans", response_model=List[api_schemas.PlanResponse], status_code=status.HTTP_200_OK)
def get_plans(skip : int = 0, limit : int = 100, db : Session = Depends(get_db)):
    plans = db.query(models.Plan).offset(skip).limit(limit).all()
    if not plans:
        raise HTTPException(status_code=404, detail="No plans found")
    return plans

@router.post("/makeplan", response_model=api_schemas.PlanResponse, status_code=status.HTTP_201_CREATED)
def create_plan(plan: api_schemas.PlanCreate, db: Session = Depends(get_db)):
    db_plan = db.query(models.Plan).filter(models.Plan.name == plan.name).first()
    if db_plan:
        raise HTTPException(status_code=400, detail="Plan name already exists")

    db_plan = models.Plan(
        name=plan.name,
        description=plan.description,
        amount=plan.amount,
        currency=plan.currency,
        interval=plan.interval,
        is_active=plan.is_active
    )
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan