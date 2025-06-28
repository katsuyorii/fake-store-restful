from fastapi import APIRouter, Depends, status

from products.schemas.sizes import SizeResponseSchema, SizeCreateSchema, SizeUpdateSchema
from products.services.sizes import ProductSizesService
from products.dependencies import get_product_sizes_service


sizes_router = APIRouter(
    prefix='/sizes',
    tags=['Sizes'],
)

@sizes_router.get('', response_model=list[SizeResponseSchema])
async def get_all_sizes(skip: int | None = None, limit: int | None = None, product_sizes_service: ProductSizesService = Depends(get_product_sizes_service)):
    return await product_sizes_service.get_all_sizes(skip, limit)

@sizes_router.get('/{size_id}', response_model=SizeResponseSchema)
async def get_size(size_id: int, product_sizes_service: ProductSizesService = Depends(get_product_sizes_service)):
    return await product_sizes_service.get_size(size_id)

@sizes_router.post('', status_code=status.HTTP_201_CREATED, response_model=SizeResponseSchema)
async def create_size(size_data: SizeCreateSchema, product_sizes_service: ProductSizesService = Depends(get_product_sizes_service)):
    return await product_sizes_service.create_size(size_data)

@sizes_router.patch('/{size_id}', response_model=SizeResponseSchema)
async def update_size(size_id: int, size_updated_data: SizeUpdateSchema, product_sizes_service: ProductSizesService = Depends(get_product_sizes_service)):
    return await product_sizes_service.update_size(size_id, size_updated_data)

@sizes_router.delete('/{size_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_size(size_id: int, product_sizes_service: ProductSizesService = Depends(get_product_sizes_service)):
    return await product_sizes_service.delete_size(size_id)