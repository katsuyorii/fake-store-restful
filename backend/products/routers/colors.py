from fastapi import APIRouter, Depends, status

from products.schemas.colors import ColorResponseSchema, ColorCreateSchema, ColorUpdateSchema
from products.services.colors import ProductColorsService
from products.dependencies import get_product_colors_service


colors_router = APIRouter(
    prefix='/colors',
    tags=['Colors'],
)

@colors_router.get('', response_model=list[ColorResponseSchema])
async def get_all_colors(skip: int | None = None, limit: int | None = None, product_colors_service: ProductColorsService = Depends(get_product_colors_service)):
    return await product_colors_service.get_all_colors(skip, limit)

@colors_router.get('/{color_id}', response_model=ColorResponseSchema)
async def get_color(color_id: int, product_colors_service: ProductColorsService = Depends(get_product_colors_service)):
    return await product_colors_service.get_color(color_id)

@colors_router.post('', status_code=status.HTTP_201_CREATED, response_model=ColorResponseSchema)
async def create_color(color_data: ColorCreateSchema, product_colors_service: ProductColorsService = Depends(get_product_colors_service)):
    return await product_colors_service.create_color(color_data)

@colors_router.patch('/{color_id}', response_model=ColorResponseSchema)
async def update_color(color_id: int, color_updated_data: ColorUpdateSchema, product_colors_service: ProductColorsService = Depends(get_product_colors_service)):
    return await product_colors_service.update_color(color_id, color_updated_data)

@colors_router.delete('/{color_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_color(color_id: int, product_colors_service: ProductColorsService = Depends(get_product_colors_service)):
    return await product_colors_service.delete_color(color_id)