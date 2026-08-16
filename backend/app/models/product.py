from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func, UUID, String, DateTime, ForeignKey, Numeric, PrimaryKeyConstraint
from app.core.database import Base
import uuid
from datetime import datetime
from decimal import Decimal


class Product(Base):
    __tablename__="products"
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    rozetka_id: Mapped[int] = mapped_column(nullable=False, unique=True, index=True)
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    href: Mapped[str] = mapped_column(String(300), nullable=False)
    brand: Mapped[str] = mapped_column(String(250))
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    image_url: Mapped[str] = mapped_column(String(300))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    

class TrackedProduct(Base):
    __tablename__="tracked_products"
    __table_args__=(PrimaryKeyConstraint("user_id", "product_id"),)
    
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"), nullable=False)