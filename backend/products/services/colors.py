from products.repositories.colors import ProductColorsRepository


class ProductColorsService:
    def __init__(self, product_colors_repository: ProductColorsRepository):
        self.product_colors_repository = product_colors_repository