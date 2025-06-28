from pydantic import BaseModel, Field

from datetime import datetime

from decimal import Decimal

from products.schemas.categories import CategoryResponseSchema
from products.schemas.brands import BrandResponseSchema
from products.schemas.colors import ColorResponseSchema
from products.schemas.sizes import SizeResponseSchema


class ProductResponseSchema(BaseModel):
    id: int
    title: str
    slug: str
    description: str
    price: Decimal
    discount_percent: int | None
    amount: int
    sales: int
    is_active: bool
    category: CategoryResponseSchema
    brand: BrandResponseSchema
    sizes: list[SizeResponseSchema]
    colors: list[ColorResponseSchema]
    created_at: datetime
    updated_at: datetime


class ProductCreateSchema(BaseModel):
    title: str
    description: str
    price: Decimal
    discount_percent: int | None = Field(default=None)
    amount: int
    category_id: int
    brand_id: int
    sizes: list[int]
    colors: list[int]
