from sqlalchemy import DateTime, String, func, CheckConstraint, Numeric, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime

from decimal import Decimal

from core.models.base import BaseModel


products_colors_assoc = Table(
    "products_colors_assoc",
    BaseModel.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("color_id", ForeignKey("colors.id"), primary_key=True)
)

products_sizes_assoc = Table(
    "products_sizes_assoc",
    BaseModel.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("size_id", ForeignKey("sizes.id"), primary_key=True)
)


class ProductCategoryModel(BaseModel):
    __tablename__ = 'categories'

    name: Mapped[str] = mapped_column(String(128), unique=True, index=True)
    slug: Mapped[str] = mapped_column(String(256))

    products: Mapped[list["ProductModel"]] = relationship(back_populates='category')


class ProductBrandModel(BaseModel):
    __tablename__ = 'brands'

    name: Mapped[str] = mapped_column(String(128), unique=True, index=True)
    slug: Mapped[str] = mapped_column(String(256))

    products: Mapped[list["ProductModel"]] = relationship(back_populates='brand')


class ProductSizeModel(BaseModel):
    __tablename__ = 'sizes'

    name: Mapped[str] = mapped_column(String(128), unique=True, index=True)

    products: Mapped[list['ProductModel']] = relationship(secondary=products_sizes_assoc, back_populates='sizes')


class ProductColorModel(BaseModel):
    __tablename__ = 'colors'
    
    name: Mapped[str] = mapped_column(String(128), unique=True, index=True)

    products: Mapped[list['ProductModel']] = relationship(secondary=products_colors_assoc, back_populates='colors')


class ProductModel(BaseModel):
    __tablename__ = 'products'

    title: Mapped[str] = mapped_column(String(128), unique=True, index=True)
    slug: Mapped[str] = mapped_column(String(256))
    description: Mapped[str]
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), CheckConstraint('price >= 0.00'), default=Decimal('0.00'))
    discount_percent: Mapped[int] = mapped_column(CheckConstraint('discount_percent >= 0'), nullable=True)
    amount: Mapped[int] = mapped_column(CheckConstraint('amount >= 0'), default=0)
    sales: Mapped[int] = mapped_column(CheckConstraint('sales >= 0'), default=0)

    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), index=True)
    category: Mapped[ProductCategoryModel] = relationship(back_populates='products')
    brand_id: Mapped[int] = mapped_column(ForeignKey('brands.id'), index=True)
    brand: Mapped[ProductBrandModel] = relationship(back_populates='products')

    sizes: Mapped[list['ProductSizeModel']] = relationship(secondary=products_sizes_assoc, back_populates='products')
    colors: Mapped[list['ProductColorModel']] = relationship(secondary=products_colors_assoc, back_populates='products')

    is_active: Mapped[bool] = mapped_column(default=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
