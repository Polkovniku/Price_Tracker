from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID
from decimal import Decimal


class PriceHistoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: UUID
    product_id: UUID
    price: Decimal
    recorded_at: datetime
    
class PriceHistoryCreate(BaseModel):
    product_id: UUID
    price: Decimal = Field(max_digits=10, decimal_places=2)