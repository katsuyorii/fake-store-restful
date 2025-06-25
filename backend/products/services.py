from .repositories import ProductCategoriesRepository, ProductManufacturersRepository


class ProductCategoriesService:
    def __init__(self, product_categories_repository: ProductCategoriesRepository):
        self.product_categories_repository = product_categories_repository


class ProductManufacturersService:
    def __init__(self, product_manufacturers_repository: ProductManufacturersRepository):
        self.product_manufacturers_repository = product_manufacturers_repository