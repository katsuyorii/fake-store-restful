from .repositories import ProductCategoriesRepository, ProductManufacturersRepository

from .schemas import CategoryCreateSchema
from .models import ProductCategory


class ProductCategoriesService:
    def __init__(self, product_categories_repository: ProductCategoriesRepository):
        self.product_categories_repository = product_categories_repository
    
    async def create_category(self, category_data: CategoryCreateSchema) -> ProductCategory:
        return await self.product_categories_repository.create(category_data.model_dump(exclude_unset=True))


class ProductManufacturersService:
    def __init__(self, product_manufacturers_repository: ProductManufacturersRepository):
        self.product_manufacturers_repository = product_manufacturers_repository