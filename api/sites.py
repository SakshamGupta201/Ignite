from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import models
from database.database import SessionLocal
from schemas import schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sites/", response_model=schemas.SiteResponse)
async def create_site(site: schemas.SiteCreate, db: Session = Depends(get_db)):
    db_site = models.Site(**site.dict())
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return db_site

@router.get("/sites/{site_id}", response_model=schemas.SiteResponse)
async def read_site(site_id: int, db: Session = Depends(get_db)):
    db_site = db.query(models.Site).filter(models.Site.id == site_id).first()
    if db_site is None:
        raise HTTPException(status_code=404, detail="Site not found")
    return db_site

@router.get("/sites/", response_model=list[schemas.SiteResponse])
async def read_sites(db: Session = Depends(get_db)):
    sites = db.query(models.Site).all()
    return sites

@router.put("/sites/{site_id}", response_model=schemas.SiteResponse)
async def update_site(site_id: int, site: schemas.SiteUpdate, db: Session = Depends(get_db)):
    db_site = db.query(models.Site).filter(models.Site.id == site_id).first()
    if db_site is None:
        raise HTTPException(status_code=404, detail="Site not found")
    for attr, value in site.dict().items():
        setattr(db_site, attr, value)
    db.commit()
    db.refresh(db_site)
    return db_site

@router.delete("/sites/{site_id}")
async def delete_site(site_id: int, db: Session = Depends(get_db)):
    db_site = db.query(models.Site).filter(models.Site.id == site_id).first()
    if db_site is None:
        raise HTTPException(status_code=404, detail="Site not found")
    db.delete(db_site)
    db.commit()
    return {"message": "Site deleted successfully"}
