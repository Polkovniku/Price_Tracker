from fastapi import APIRouter, Depends
from app.schemas.users import UserResponse
from app.services.users import UserService
from app.core.dependencies import get_db, get_current_user
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.users import User


router = APIRouter(prefix="/users", tags=["users"])

def get_user_service(db: Annotated[AsyncSession, Depends(get_db)]):
    return UserService(db)

@router.get("/me", response_model=UserResponse)
async def get_me(user: Annotated[User, Depends(get_current_user)]):
    return user

@router.delete("/me")
async def delete_user(user_service: Annotated[UserService, Depends(get_user_service)], user: Annotated[User, Depends(get_current_user)]):
    return await user_service.delete_user(user.id)