from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.dependencies.database import get_db

from .repositories import ProductCategoriesRepository, ProductManufacturersRepository
from .services import ProductCategoriesService


def get_product_categories_repository(db: AsyncSession = Depends(get_db)) -> ProductCategoriesRepository:
    return ProductCategoriesRepository(db)

def get_product_manufacturers_repository(db: AsyncSession = Depends(get_db)) -> ProductManufacturersRepository:
    return ProductManufacturersRepository(db)

def get_product_categories_service(product_categories_repository: ProductCategoriesRepository = Depends(get_product_categories_repository)):
    return ProductCategoriesService(product_categories_repository)