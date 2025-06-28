from sqlalchemy import DateTime, String, func, CheckConstraint, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime

from decimal import Decimal

from core.models.base import BaseModel


class ProductCategoryModel(BaseModel):
    __tablename__ = 'categories'

    name: Mapped[str] = mapped_column(String(128), unique=True, index=True)
    slug: Mapped[str] = mapped_column(String(256))

    products: Mapped[list["ProductModel"]] = relationship(back_populates='category')


class ProductModel(BaseModel):
    __tablename__ = 'products'

    title: Mapped[str] = mapped_column(String(128), unique=True, index=True)
    slug: Mapped[str] = mapped_column(String(256))
    description: Mapped[str]
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), CheckConstraint('price >= 0.00'), default=Decimal('0.00'))
    discount_percent: Mapped[int] = mapped_column(CheckConstraint('discount_percent >= 0'), nullable=True)
    amount: Mapped[int] = mapped_column(CheckConstraint('amount >= 0'), default=0)

    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), index=True)
    category: Mapped[ProductCategoryModel] = relationship(back_populates='products')

    is_active: Mapped[bool] = mapped_column(default=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
