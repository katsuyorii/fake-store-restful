from pydantic import BaseModel, Field, EmailStr, field_validator

from datetime import datetime, date

from core.utils.validators import validation_valid_phone_number

from .models import UserRoleEnum, UserGenderEnum


class UserUpdateSchema(BaseModel):
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    phone_number: str | None = Field(default=None)
    birthday: date |None = Field(default=None)
    gender: UserGenderEnum |None = Field(default=None)
    is_mailing: bool

    @field_validator('phone_number')
    @classmethod
    def validate_phone_number(cls, value: str) -> str:
        return validation_valid_phone_number(value)


class UserResponseSchema(BaseModel):
    id: int
    email: EmailStr
    role: UserRoleEnum
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    phone_number: str | None = Field(default=None)
    birthday: date |None = Field(default=None)
    gender: UserGenderEnum |None = Field(default=None)
    created_at: datetime
    updated_at: datetime
    is_active: bool
    is_mailing: bool


class UserAddressResponseSchema(BaseModel):
    id: int
    user_id: int
    street: str
    house: str
    entrance: str | None
    floor: int | None
    apartment: int
    intercom: str | None
    comment: str | None


class UserAddressCreateSchema(BaseModel):
    user_id: int
    street: str
    house: str
    entrance: str | None = Field(default=None)
    floor: int | None = Field(default=None)
    apartment: int
    intercom: str | None = Field(default=None)
    comment: str | None = Field(default=None)