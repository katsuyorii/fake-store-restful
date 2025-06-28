from core.repositories.database_base import DatabaseBaseRepository

from products.models import ProductColorModel


class ProductColorsRepository(DatabaseBaseRepository):
    def __init__(self, db, model: ProductColorModel = ProductColorModel):
        super().__init__(db, model)