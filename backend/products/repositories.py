from sqlalchemy.ext.asyncio import AsyncSession

from core.repositories.database_base import DatabaseBaseRepository

from .models import ProductCategory, ProductManufacturer


class ProductCategoriesRepository(DatabaseBaseRepository):
    def _init__(self, db: AsyncSession, model: ProductCategory = ProductCategory):
        super().__init__(db, model)


class ProductManufacturersRepository(DatabaseBaseRepository):
    def _init__(self, db: AsyncSession, model: ProductManufacturer = ProductManufacturer):
        super().__init__(db, model)