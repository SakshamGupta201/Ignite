# models.py

from sqlalchemy import Column, Integer, String
from database.database import Base, engine

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    platform_name = Column(String)
    vendor_name = Column(String)
    organisation_name = Column(String)
    

class Site(Base):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True, index=True)
    organization_name = Column(String(length=255))
    site_name = Column(String(length=255))
    site_type = Column(String(length=50))
    site_region = Column(String(length=50))
    hub_id = Column(String(length=50), nullable=True)
    sal_code = Column(String(length=50))
    site_address = Column(String(length=255))
    country = Column(String(length=50))
    city = Column(String(length=50))
    network_name = Column(String(length=255))
    site_tag = Column(String(length=50))
    time_zone = Column(String(length=50))
    license_shared = Column(String(length=50))


Base.metadata.create_all(bind=engine)