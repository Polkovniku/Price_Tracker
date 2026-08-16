import asyncio
from app.core.celery_app import celery_app
from app.models.product import Product
from sqlalchemy import select, update
from camoufox.async_api import AsyncCamoufox
from app.services.scraper import fetch_product
from app.models.price_history import PriceHistory
from sqlalchemy.exc import SQLAlchemyError
import logging
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.pool import NullPool
from app.core.config import settings

celery_engine = create_async_engine(url=settings.database_url, poolclass=NullPool)
CelerySession = async_sessionmaker(bind=celery_engine, expire_on_commit=False)


@celery_app.task
def check_prices():
    asyncio.run(_check_prices())
    
async def _check_prices():
    async with AsyncCamoufox(headless=True) as browser:
        page = await browser.new_page()
        async with CelerySession() as db:
            products = (await db.execute(select(Product.id, Product.rozetka_id, Product.price))).all()
            
            for product in products:
                data = await fetch_product(product.rozetka_id, page)
                new_price = data["price"]
                
                if new_price == product.price:
                    continue
                
                price_history = PriceHistory(product_id=product.id, price=new_price)
                db.add(price_history)
                
                await db.execute(update(Product).where(Product.id == product.id).values(price=new_price))
                
            try:
                await db.commit()
            except SQLAlchemyError as e:
                await db.rollback()
                logging.error(f"Price check failed: {e}")