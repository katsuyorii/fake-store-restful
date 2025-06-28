from fastapi import APIRouter, Depends, status

from products.schemas.brands import BrandResponseSchema, BrandCreateSchema, BrandUpdateSchema
from products.services.brands import ProductBrandsService
from products.dependencies import get_product_brands_service


brands_router = APIRouter(
    prefix='/brands',
    tags=['Brands'],
)

@brands_router.get('', response_model=list[BrandResponseSchema])
async def get_all_brands(skip: int | None = None, limit: int | None = None, product_brand_service: ProductBrandsService = Depends(get_product_brands_service)):
    return await product_brand_service.get_all_brands(skip, limit)

@brands_router.get('/{brand_id}', response_model=BrandResponseSchema)
async def get_brand(brand_id: int, product_brand_service: ProductBrandsService = Depends(get_product_brands_service)):
    return await product_brand_service.get_brand(brand_id)

@brands_router.post('', status_code=status.HTTP_201_CREATED, response_model=BrandResponseSchema)
async def create_brand(brand_data: BrandCreateSchema, product_brand_service: ProductBrandsService = Depends(get_product_brands_service)):
    return await product_brand_service.create_brand(brand_data)

@brands_router.patch('/{brand_id}', response_model=BrandResponseSchema)
async def update_brand(brand_id: int, brand_updated_data: BrandUpdateSchema, product_brand_service: ProductBrandsService = Depends(get_product_brands_service)):
    return await product_brand_service.update_brand(brand_id, brand_updated_data)

@brands_router.delete('/{brand_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_brand(brand_id: int, product_brand_service: ProductBrandsService = Depends(get_product_brands_service)):
    return await product_brand_service.delete_brand(brand_id)