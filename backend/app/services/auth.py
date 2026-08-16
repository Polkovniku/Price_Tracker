from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.users import UserCreate, UserLogin
from app.models.users import User
from app.core.security import hashed_password, verify_password, create_access_token, create_refresh_token, decode_token
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from fastapi import HTTPException, status
from app.services.users import UserService
from uuid import UUID

class AuthService:
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def create_user(self, data: UserCreate) -> User:
        data = data.model_dump()
        password = data.pop("password")
        password_hash = hashed_password(password)
        user = User(hash_password=password_hash, **data)
        try: 
            self.db.add(user)
            await self.db.commit()
            await self.db.refresh(user)
            return user
        except IntegrityError:
            await self.db.rollback()
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")
        except SQLAlchemyError:
            await self.db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Invalid create user")
        
    async def log_in(self, data: UserLogin):
        user_service = UserService(self.db)
        user = await user_service.get_user_by_email(data.email)
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
        check_password = verify_password(data.password, user.hash_password)
        if not check_password:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
        payload = {"sub": str(user.id)}
        access_token = create_access_token(payload)
        refresh_token = create_refresh_token(payload)
        return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}
        
    async def update_token(self, token: str):
        try:
            payload = decode_token(token)
        except Exception:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        if payload.get("type") != "refresh":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type")
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")
        
        service = UserService(self.db)
        user = await service.get_user_by_id(UUID(user_id))
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User is not found")
        payload = {"sub": str(user.id)}
        access_token = create_access_token(payload)
        refresh_token = create_refresh_token(payload)
        return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}
        