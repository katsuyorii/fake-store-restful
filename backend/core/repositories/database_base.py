from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class DatabaseBaseRepository:
    def __init__(self, db: AsyncSession, model):
        self.db = db
        self.model = model
    
    async def create(self, obj_data: dict):
        obj = self.model(**obj_data)
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj
    
    async def get_all(self, skip: int = 0, limit: int = 5):
        objs = await self.db.execute(select(self.model).offset(skip).limit(limit))
        return objs.scalars().all()
    
    async def get_by_id(self, id: int):
        obj = await self.db.execute(select(self.model).where(self.model.id == id))
        return obj.scalar_one_or_none()
    
    async def update(self, obj, updated_obj_data: dict):
        for key, value in updated_obj_data.items():
            setattr(obj, key, value)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj
    
    async def delete(self, obj):
        await self.db.delete(obj)
        await self.db.commit()