from .repositories import ProductCategoriesRepository

from .schemas import CategoryCreateSchema, CategoryUpdateSchema
from .models import ProductCategoryModel
from .exceptions import CategoryNotFound


class ProductCategoriesService:
    def __init__(self, product_categories_repository: ProductCategoriesRepository):
        self.product_categories_repository = product_categories_repository
    
    async def get_all_categories(self, skip: int | None = None, limit: int | None = None) -> list[ProductCategoryModel]:
        return await self.product_categories_repository.get_all(skip, limit)
    
    async def get_category(self, category_id: int) -> ProductCategoryModel | None:
        category = await self.product_categories_repository.get_by_id(category_id)

        if not category:
            raise CategoryNotFound()

        return category
        
    async def create_category(self, category_data: CategoryCreateSchema) -> ProductCategoryModel:
        return await self.product_categories_repository.create(category_data.model_dump(exclude_unset=True))
    
    async def update_category(self, category_id: int, category_updated_data: CategoryUpdateSchema) -> ProductCategoryModel | None:
        category = await self.product_categories_repository.get_by_id(category_id)

        if not category:
            raise CategoryNotFound()
        
        return await self.product_categories_repository.update(category, category_updated_data.model_dump(exclude_unset=True))
    
    async def delete_category(self, category_id: int) -> None:
        category = await self.product_categories_repository.get_by_id(category_id)

        if not category:
            raise CategoryNotFound()
        
        await self.product_categories_repository.delete(category)