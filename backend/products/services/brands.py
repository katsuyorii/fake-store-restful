from products.repositories.brands import ProductBrandsRepository
from products.schemas.brands import BrandCreateSchema, BrandUpdateSchema
from products.exceptions import BrandNotFound
from products.models import ProductBrandModel


class ProductBrandsService:
    def __init__(self, product_brands_repository: ProductBrandsRepository):
        self.product_brands_repository = product_brands_repository
    
    async def get_all_brands(self, skip: int | None = None, limit: int | None = None) -> list[ProductBrandModel]:
        return await self.product_brands_repository.get_all(skip, limit)
    
    async def get_brand(self, brand_id: int) -> ProductBrandModel | None:
        brand = await self.product_brands_repository.get_by_id(brand_id)

        if not brand:
            raise BrandNotFound()

        return brand

    async def create_brand(self, brand_data: BrandCreateSchema) -> ProductBrandModel:
        return await self.product_brands_repository.create(brand_data.model_dump(exclude_unset=True))

    async def update_brand(self, brand_id: int, brand_updated_data: BrandUpdateSchema) -> ProductBrandModel | None:
        brand = await self.product_brands_repository.get_by_id(brand_id)

        if not brand:
            raise BrandNotFound()
        
        return await self.product_brands_repository.update(brand, brand_updated_data.model_dump(exclude_unset=True))
    
    async def delete_brand(self, brand_id: int) -> None:
        brand = await self.product_brands_repository.get_by_id(brand_id)

        if not brand:
            raise BrandNotFound()
        
        await self.product_brands_repository.delete(brand)