from fastapi import APIRouter, Depends
from app.schemas.users import UserLogin, UserResponse, UserCreate, TokenRequest, TokenResponse
from app.services.auth import AuthService
from app.core.dependencies import get_db
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/auth", tags=["auth"])

def get_auth_service(db: Annotated[AsyncSession, Depends(get_db)]):
    return AuthService(db)

@router.post("/register", response_model=UserResponse)
async def sign_up(data: UserCreate, auth_service: Annotated[AuthService, Depends(get_auth_service)]):
    return await auth_service.create_user(data)

@router.post("/login", response_model=TokenResponse)
async def sign_in(data: UserLogin, auth_service: Annotated[AuthService, Depends(get_auth_service)]):
    return await auth_service.log_in(data)

@router.post("/refresh", response_model=TokenResponse)
async def update_tokens(data: TokenRequest, auth_service: Annotated[AuthService, Depends(get_auth_service)]):
    return await auth_service.update_token(data)