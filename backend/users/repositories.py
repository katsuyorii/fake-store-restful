from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.repositories.database_base import DatabaseBaseRepository

from .models import UserModel, UserAddressModel


class UsersAddressesRepository(DatabaseBaseRepository):
    def __init__(self, db: AsyncSession, model: UserAddressModel = UserAddressModel):
        super().__init__(db, model)
    
    async def get_all(self, user_id: int, skip: int = 0, limit: int = 5) -> list[UserAddressModel]:
        objs = await self.db.execute(select(self.model).where(self.model.user_id == user_id).offset(skip).limit(limit))
        return objs.scalars().all()
    
    async def get_by_id(self, user_id: int, address_id: int) -> UserAddressModel | None:
        obj = await self.db.execute(select(self.model).where(self.model.id == address_id).where(self.model.user_id == user_id))
        return obj.scalar_one_or_none()


class UsersRepository(DatabaseBaseRepository):
    def __init__(self, db: AsyncSession, model: UserModel = UserModel):
        super().__init__(db, model)
    
    async def get_by_email(self, email: str) -> UserModel | None:
        result = await self.db.execute(select(UserModel).where(UserModel.email == email))
        return result.scalar_one_or_none()