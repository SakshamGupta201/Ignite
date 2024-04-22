from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import models
from database.database import SessionLocal
from schemas import schemas

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/customers/", response_model=schemas.CustomerResponse)
async def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@router.get("/customers/", response_model=list[schemas.CustomerResponse])
async def read_customers(db: Session = Depends(get_db)):
    customers = db.query(models.Customer).all()
    return customers
