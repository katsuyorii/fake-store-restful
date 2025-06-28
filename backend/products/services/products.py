from products.repositories.products import ProductsRepository


class ProductService:
    def __init__(self, products_repository: ProductsRepository):
        self.products_repository = products_repository