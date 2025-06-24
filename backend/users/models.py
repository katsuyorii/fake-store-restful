from sqlalchemy import DateTime, String, func, CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime, date
from enum import Enum

from core.models.base import BaseModel


class UserRoleEnum(str, Enum):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class UserGenderEnum(str, Enum):
    MALE = 'male'
    FEMALE = 'female'


class UserModel(BaseModel):
    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str]
    role: Mapped[UserRoleEnum] = mapped_column(default=UserRoleEnum.USER)

    first_name: Mapped[str] = mapped_column(String(128), nullable=True)
    last_name: Mapped[str] = mapped_column(String(128), nullable=True)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=True)
    birthday: Mapped[date] = mapped_column(nullable=True)
    gender: Mapped[UserGenderEnum] = mapped_column(nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    is_active: Mapped[bool] = mapped_column(default=False)
    is_mailing: Mapped[bool] = mapped_column(default=True)

    addresses: Mapped[list["UserAddressModel"]] = relationship(back_populates='user')


class UserAddressModel(BaseModel):
    __tablename__ = 'users_addresses'

    street: Mapped[str] = mapped_column(String(256))
    house: Mapped[str] = mapped_column(String(15))
    entrance: Mapped[str] = mapped_column(CheckConstraint("entrance >= 0"), nullable=True)
    floor: Mapped[int] = mapped_column(CheckConstraint("floor >= 0"), nullable=True)
    apartment: Mapped[int] = mapped_column(CheckConstraint("apartment > 0"))
    intercom: Mapped[str] = mapped_column(String(20), nullable=True)
    comment: Mapped[str] = mapped_column(nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), index=True)
    user: Mapped[UserModel] = relationship(back_populates='addresses')