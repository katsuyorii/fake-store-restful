from sqlalchemy.ext.asyncio import AsyncSession

from slugify import slugify

from core.repositories.database_base import DatabaseBaseRepository

from .models import ProductCategoryModel, ProductBrandModel, ProductSizeModel, ProductColorModel


class ProductCategoriesRepository(DatabaseBaseRepository):
    def __init__(self, db: AsyncSession, model: ProductCategoryModel = ProductCategoryModel):
        super().__init__(db, model)
    
    async def create(self, obj_data: dict):
        obj_data['slug'] = slugify(obj_data.get('name'))
        obj = self.model(**obj_data)
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj
    
    async def update(self, obj, updated_obj_data: dict):
        updated_obj_data['slug'] = slugify(updated_obj_data.get('name'))
        for key, value in updated_obj_data.items():
            setattr(obj, key, value)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj


class ProductBrandsRepository(ProductCategoriesRepository):
    def __init__(self, db, model: ProductBrandModel = ProductBrandModel):
        super().__init__(db, model)


class ProductSizesRepository(DatabaseBaseRepository):
    def __init__(self, db, model: ProductSizeModel = ProductSizeModel):
        super().__init__(db, model)


class ProductColorsRepository(DatabaseBaseRepository):
    def __init__(self, db, model: ProductColorModel = ProductColorModel):
        super().__init__(db, model)