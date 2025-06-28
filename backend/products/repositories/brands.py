from products.models import  ProductBrandModel
from products.repositories.categories import ProductCategoriesRepository


class ProductBrandsRepository(ProductCategoriesRepository):
    def __init__(self, db, model: ProductBrandModel = ProductBrandModel):
        super().__init__(db, model)