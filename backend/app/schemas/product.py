from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID
from decimal import Decimal

class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: UUID
    rozetka_id: int
    title: str
    href: str
    brand: str
    price: Decimal
    image_url: str
    created_at: datetime
    
class ProductCreate(BaseModel):
    rozetka_id: int
    title: str = Field(min_length=5, max_length=500)
    href: str = Field(min_length=10, max_length=300)
    brand: str = Field(min_length=2, max_length=250)
    price: Decimal = Field(max_digits=10, decimal_places=2)
    image_url: str = Field(min_length=10, max_length=300)

class ProductAdd(BaseModel):
    href: str