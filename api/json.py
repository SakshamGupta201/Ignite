from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import models
from database.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class DataItem(BaseModel):
    key: str
    value: dict

@router.post("/store/")
async def store_data(data_item: DataItem, db: Session = Depends(get_db)):
    db_item = models.DataItem(**data_item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"message": "Data stored successfully", "entry": db_item}
@router.get("/data/")
async def get_data(db: Session = Depends(get_db)):
    return db.query(models.DataItem).all()