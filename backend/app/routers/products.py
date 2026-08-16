from uuid import UUID
from fastapi import APIRouter, Depends
from app.schemas.product import ProductAdd, ProductCreate, ProductResponse
from app.services.products import ProductService
from app.core.dependencies import get_db, get_current_user
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.users import User
from fastapi import Request

router = APIRouter(prefix="/products", tags=["products"])

def get_page(request: Request):
    return request.app.state.page

def get_product_service(db: Annotated[AsyncSession, Depends(get_db)]):
    return ProductService(db)

@router.post("/", response_model=ProductResponse)
async def create_product(
    data: ProductAdd, 
    user: Annotated[User, Depends(get_current_user)],
    product_service: Annotated[ProductService, Depends(get_product_service)],
    page = Depends(get_page)
):
    return await product_service.add_product(data.href, user.id, page)

@router.get("/", response_model=list[ProductResponse])
async def get_products(user: Annotated[User, Depends(get_current_user)], product_service: Annotated[ProductService, Depends(get_product_service)]):
    return await product_service.get_products(user.id)

@router.get("/search", response_model=list[dict])
async def search_product(
    text: str, 
    product_service: Annotated[ProductService, Depends(get_product_service)],
    page = Depends(get_page)
):
    return await product_service.search_products(text, page)

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(
    product_id: UUID, 
    user: Annotated[User, Depends(get_current_user)],
    product_service: Annotated[ProductService, Depends(get_product_service)]
):
    return await product_service.get_product_by_id(product_id, user.id)

@router.delete("/{product_id}")
async def delete_product(
    product_id: UUID, 
    user: Annotated[User, Depends(get_current_user)],
    product_service: Annotated[ProductService, Depends(get_product_service)]
):
    return await product_service.remove_product(product_id, user.id)
