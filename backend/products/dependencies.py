from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.dependencies.database import get_db

from products.repositories.categories import ProductCategoriesRepository
from products.repositories.brands import ProductBrandsRepository
from products.repositories.sizes import ProductSizesRepository
from products.repositories.colors import ProductColorsRepository
from products.services.categories import ProductCategoriesService
from products.services.brands import ProductBrandsService
from products.services.sizes import ProductSizesService
from products.services.colors import ProductColorsService


def get_product_categories_repository(db: AsyncSession = Depends(get_db)) -> ProductCategoriesRepository:
    return ProductCategoriesRepository(db)

def get_product_brands_repository(db: AsyncSession = Depends(get_db)) -> ProductBrandsRepository:
    return ProductBrandsRepository(db)

def get_product_sizes_repository(db: AsyncSession = Depends(get_db)) -> ProductSizesRepository:
    return ProductSizesRepository(db)

def get_product_colors_repository(db: AsyncSession = Depends(get_db)) -> ProductColorsRepository:
    return ProductColorsRepository(db)

def get_product_categories_service(product_categories_repository: ProductCategoriesRepository = Depends(get_product_categories_repository)):
    return ProductCategoriesService(product_categories_repository)

def get_product_brands_service(product_brands_repository: ProductBrandsRepository = Depends(get_product_brands_repository)):
    return ProductBrandsService(product_brands_repository)

def get_product_sizes_service(product_sizes_repository: ProductSizesRepository = Depends(get_product_sizes_repository)):
    return ProductSizesService(product_sizes_repository)

def get_product_colors_service(product_colors_repository: ProductBrandsRepository = Depends(get_product_colors_repository)):
    return ProductColorsService(product_colors_repository)