from products.repositories.sizes import ProductSizesRepository
from products.schemas.sizes import SizeCreateSchema, SizeUpdateSchema
from products.models import ProductSizeModel
from products.exceptions import SizeNotFound


class ProductSizesService:
    def __init__(self, product_sizes_repository: ProductSizesRepository):
        self.product_sizes_repository = product_sizes_repository
    
    async def get_all_sizes(self, skip: int | None = None, limit: int | None = None) -> list[ProductSizeModel]:
        sizes = await self.product_sizes_repository.get_all(skip, limit)

        return sizes
    
    async def get_size(self, size_id: int) -> ProductSizeModel | None:
        size = await self.product_sizes_repository.get_by_id(size_id)

        if not size:
            raise SizeNotFound()
        
        return size
    
    async def create_size(self, sizes_data: SizeCreateSchema) -> ProductSizeModel:
        new_size = await self.product_sizes_repository.create(sizes_data.model_dump(exclude_unset=True))

        return new_size
    
    async def update_size(self, size_id: int, size_updated_data: SizeUpdateSchema) -> ProductSizeModel | None:
        size = await self.product_sizes_repository.get_by_id(size_id)

        if not size:
            raise SizeNotFound()
        
        await self.product_sizes_repository.update(size, size_updated_data.model_dump(exclude_unset=True))

        return size
    
    async def delete_size(self, size_id: int) -> None:
        size = await self.product_sizes_repository.get_by_id(size_id)

        if not size:
            raise SizeNotFound()
        
        await self.product_sizes_repository.delete(size)