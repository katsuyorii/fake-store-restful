from .repositories import ProductCategoriesRepository, ProductManufacturersRepository

from .schemas import CategoryCreateSchema
from .models import ProductCategory
from .exceptions import CategoryNotFound


class ProductCategoriesService:
    def __init__(self, product_categories_repository: ProductCategoriesRepository):
        self.product_categories_repository = product_categories_repository
    
    async def get_all_categories(self, skip: int | None = None, limit: int | None = None) -> list[ProductCategory]:
        return await self.product_categories_repository.get_all(skip, limit)
    
    async def get_category(self, category_id: int) -> ProductCategory | None:
        category = await self.product_categories_repository.get_by_id(category_id)

        if not category:
            raise CategoryNotFound()

        return category
        
    async def create_category(self, category_data: CategoryCreateSchema) -> ProductCategory:
        return await self.product_categories_repository.create(category_data.model_dump(exclude_unset=True))


class ProductManufacturersService:
    def __init__(self, product_manufacturers_repository: ProductManufacturersRepository):
        self.product_manufacturers_repository = product_manufacturers_repository