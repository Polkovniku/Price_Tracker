from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import Product, TrackedProduct
from uuid import UUID
from sqlalchemy import select
from app.services.scraper import extract_rozetka_id, fetch_product, search_rozetka
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from app.models.price_history import PriceHistory

class ProductService:
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def get_product_by_id(self, product_id: UUID, user_id: UUID) -> Product | None:
        return await self.db.scalar(
            select(Product)
            .join(TrackedProduct, TrackedProduct.product_id == Product.id)
            .where(Product.id == product_id)
            .where(TrackedProduct.user_id == user_id)
        )
    
    async def get_products(self, user_id: UUID) -> list[Product]:
        return (await self.db.scalars(
            select(Product)
            .join(TrackedProduct, TrackedProduct.product_id == Product.id)
            .where(TrackedProduct.user_id == user_id)
        )).all()
        
    async def add_product(self, href: str, user_id: UUID, page):
        rozetka_id = extract_rozetka_id(href)
        
        product = await self.db.scalar(select(Product).where(Product.rozetka_id == rozetka_id))
        
        if not product:
            data = await fetch_product(rozetka_id, page)
            product = Product(
                rozetka_id=rozetka_id,
                title=data["title"],
                href=data["href"],
                brand=data["brand"],
                price=data["price"],
                image_url=data["images"]["main"]
            )
            self.db.add(product)
            await self.db.flush()
            
            price_history = PriceHistory(product_id=product.id, price=product.price)
            self.db.add(price_history)
            
        existing = await self.db.scalar(
            select(TrackedProduct)
            .where(TrackedProduct.user_id == user_id)
            .where(TrackedProduct.product_id == product.id)
        )
        if existing:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Product already tracked")    
            
        tracked = TrackedProduct(user_id=user_id, product_id=product.id)
        self.db.add(tracked)
        
        try:
            await self.db.commit()
            return product
        except SQLAlchemyError:
            await self.db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Invalide create product")
        
    async def remove_product(self, product_id: UUID, user_id: UUID):
        tracked = await self.db.scalar(
            select(TrackedProduct)
            .where(TrackedProduct.product_id == product_id)
            .where(TrackedProduct.user_id == user_id)
        )
        if not tracked:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product is not found")
        try:
            await self.db.delete(tracked)
            await self.db.commit()
        except SQLAlchemyError:
            await self.db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Invalid delete product")
        
    async def search_products(self, text: str, page):
        return await search_rozetka(text, page)
    
    async def get_price_history(self, product_id: UUID, user_id: UUID) -> list[PriceHistory]:
        product = await self.get_product_by_id(product_id, user_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product is not found")
        return (await self.db.scalars(
            select(PriceHistory)
            .where(PriceHistory.product_id == product_id)
            .order_by(PriceHistory.recorded_at)
        )).all()