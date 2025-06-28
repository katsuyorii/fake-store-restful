from products.repositories.sizes import ProductSizesRepository


class ProductSizesService:
    def __init__(self, product_sizes_repository: ProductSizesRepository):
        self.product_sizes_repository = product_sizes_repository