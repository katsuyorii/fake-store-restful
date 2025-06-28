from core.repositories.database_base import DatabaseBaseRepository

from products.models import ProductSizeModel


class ProductSizesRepository(DatabaseBaseRepository):
    def __init__(self, db, model: ProductSizeModel = ProductSizeModel):
        super().__init__(db, model)