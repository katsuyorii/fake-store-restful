from core.repositories.database_base import DatabaseBaseRepository

from products.models import ProductModel


class ProductsRepository(DatabaseBaseRepository):
    def __init__(self, db, model: ProductModel = ProductModel):
        super().__init__(db, model)