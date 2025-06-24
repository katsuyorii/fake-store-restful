from pydantic import BaseModel, Field, EmailStr

from datetime import datetime, date

from .models import UserRoleEnum, UserGenderEnum


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