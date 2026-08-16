from sqlalchemy.ext.asyncio import AsyncSession
from app.models.users import User
from sqlalchemy import select
from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_user_by_id(self, user_id: UUID) -> User | None:
        return await self.db.get(User, user_id)
    
    async def get_user_by_email(self, email: str) -> User | None:
        return await self.db.scalar(select(User).where(User.email == email))
    
    async def delete_user(self, user_id: UUID):
        user = await self.get_user_by_id(user_id)
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User is not found")
        
        try:
            await self.db.delete(user)
        except SQLAlchemyError:
            await self.db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Invalide delete user")