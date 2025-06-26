from sqlalchemy.ext.asyncio import AsyncSession

from slugify import slugify

from core.repositories.database_base import DatabaseBaseRepository

from .models import ProductCategory, ProductManufacturer


class ProductCategoriesRepository(DatabaseBaseRepository):
    def __init__(self, db: AsyncSession, model: ProductCategory = ProductCategory):
        super().__init__(db, model)
    
    async def create(self, obj_data: dict) -> ProductCategory:
        obj_data['slug'] = slugify(obj_data.get('name'))
        obj = self.model(**obj_data)
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj


class ProductManufacturersRepository(DatabaseBaseRepository):
    def __init__(self, db: AsyncSession, model: ProductManufacturer = ProductManufacturer):
        super().__init__(db, model)