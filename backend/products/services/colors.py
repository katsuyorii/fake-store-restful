from products.repositories.colors import ProductColorsRepository
from products.schemas.colors import ColorCreateSchema, ColorUpdateSchema
from products.models import ProductColorModel
from products.exceptions import ColorNotFound


class ProductColorsService:
    def __init__(self, product_colors_repository: ProductColorsRepository):
        self.product_colors_repository = product_colors_repository
    
    async def get_all_colors(self, skip: int | None = None, limit: int | None = None) -> list[ProductColorModel]:
        colors = await self.product_colors_repository.get_all(skip, limit)

        return colors
    
    async def get_color(self, color_id: int) -> ProductColorModel | None:
        color = await self.product_colors_repository.get_by_id(color_id)

        if not color:
            raise ColorNotFound()
        
        return color
    
    async def create_color(self, colors_data: ColorCreateSchema) -> ProductColorModel:
        new_color = await self.product_colors_repository.create(colors_data.model_dump(exclude_unset=True))

        return new_color
    
    async def update_color(self, color_id: int, color_updated_data: ColorUpdateSchema) -> ProductColorModel | None:
        color = await self.product_colors_repository.get_by_id(color_id)

        if not color:
            raise ColorNotFound()
        
        await self.product_colors_repository.update(color, color_updated_data.model_dump(exclude_unset=True))

        return color
    
    async def delete_color(self, color_id: int) -> None:
        color = await self.product_colors_repository.get_by_id(color_id)

        if not color:
            raise ColorNotFound()
        
        await self.product_colors_repository.delete(color)