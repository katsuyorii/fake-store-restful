from pydantic import BaseModel, EmailStr, Field, field_validator

from core.utils.validators import validation_password_complexity


class AccessTokenSchema(BaseModel):
    access_token: str
    type: str = Field(default='Bearer')


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str


class UserRegistrationSchema(UserLoginSchema):
    @field_validator('password')
    @classmethod
    def validate_password(cls, value: str) -> str:
        return validation_password_complexity(value)