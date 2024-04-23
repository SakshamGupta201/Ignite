# schemas.py


from typing import Optional
from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    name: str
    description: str

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str

class CustomerCreate(BaseModel):
    customer_name: str
    platform_name: str
    vendor_name: str
    organisation_name: str

class CustomerResponse(BaseModel):
    id: int
    customer_name: str
    platform_name: str
    vendor_name: str
    organisation_name: str
    


class SiteBase(BaseModel):
    organization_name: str
    site_name: str
    site_type: str
    site_region: str
    hub_id: Optional[str] = Field(None, nullable=True)
    sal_code: str
    site_address: str
    country: str
    city: str
    network_name: str
    site_tag: str
    time_zone: str
    license_shared: str

class SiteCreate(SiteBase):
    pass

class SiteResponse(BaseModel):
    id: int
    organization_name: str
    site_name: str
    site_type: str
    site_region: str
    hub_id: Optional[str] = Field(None, nullable=True)
    sal_code: str
    site_address: str
    country: str
    city: str
    network_name: str
    site_tag: str
    time_zone: str
    license_shared: str

class SiteUpdate(SiteBase):
    pass