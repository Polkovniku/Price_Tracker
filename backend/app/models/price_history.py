from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func, UUID, String, DateTime, ForeignKey, Numeric, PrimaryKeyConstraint
from app.core.database import Base
import uuid
from datetime import datetime
from decimal import Decimal


class PriceHistory(Base):
    __tablename__="price_history"
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)