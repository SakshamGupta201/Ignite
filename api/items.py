# api/items.py

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

@router.post("/items/", response_model=schemas.ItemResponse)
async def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/items/{item_id}", response_model=schemas.ItemResponse)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.get("/items/", response_model=list[schemas.ItemResponse])
async def read_item(db: Session = Depends(get_db)):
    db_item = db.query(models.Item).all()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
