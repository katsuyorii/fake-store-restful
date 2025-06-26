from fastapi import APIRouter, Depends, status

from .schemas import CategoryResponseSchema, CategoryCreateSchema
from .services import ProductCategoriesService
from .dependencies import get_product_categories_service


products_router = APIRouter(
    prefix='/products',
    tags=['Products'],
)

categories_router = APIRouter(
    prefix='/categories',
    tags=['Categories'],
)

manufacturers_router = APIRouter(
    prefix='/manufacturers',
    tags=['Manufacturers'],
)


@categories_router.post('', status_code=status.HTTP_201_CREATED, response_model=CategoryResponseSchema)
async def create_category(category_data: CategoryCreateSchema, product_categories_service: ProductCategoriesService = Depends(get_product_categories_service)):
    return await product_categories_service.create_category(category_data)