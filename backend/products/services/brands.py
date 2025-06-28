from products.repositories.brands import ProductBrandsRepository


class ProductBrandsService:
    def __init__(self, product_brands_repository: ProductBrandsRepository):
        self.product_brands_repository = product_brands_repository