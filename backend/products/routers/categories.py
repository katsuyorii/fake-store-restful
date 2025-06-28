from fastapi import APIRouter, Depends, status

from products.schemas.categories import CategoryResponseSchema, CategoryCreateSchema, CategoryUpdateSchema
from products.services.categories import ProductCategoriesService
from products.dependencies import get_product_categories_service


categories_router = APIRouter(
    prefix='/categories',
    tags=['Categories'],
)

@categories_router.get('', response_model=list[CategoryResponseSchema])
async def get_all_categories(skip: int | None = None, limit: int | None = None, product_categories_service: ProductCategoriesService = Depends(get_product_categories_service)):
    return await product_categories_service.get_all_categories(skip, limit)

@categories_router.get('/{category_id}', response_model=CategoryResponseSchema)
async def get_category(category_id: int, product_categories_service: ProductCategoriesService = Depends(get_product_categories_service)):
    return await product_categories_service.get_category(category_id)

@categories_router.post('', status_code=status.HTTP_201_CREATED, response_model=CategoryResponseSchema)
async def create_category(category_data: CategoryCreateSchema, product_categories_service: ProductCategoriesService = Depends(get_product_categories_service)):
    return await product_categories_service.create_category(category_data)

@categories_router.patch('/{category_id}', response_model=CategoryResponseSchema)
async def update_category(category_id: int, category_updated_data: CategoryUpdateSchema, product_categories_service: ProductCategoriesService = Depends(get_product_categories_service)):
    return await product_categories_service.update_category(category_id, category_updated_data)

@categories_router.delete('/{category_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_id: int, product_categories_service: ProductCategoriesService = Depends(get_product_categories_service)):
    return await product_categories_service.delete_category(category_id)