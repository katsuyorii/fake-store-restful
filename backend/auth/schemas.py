from pydantic import BaseModel, EmailStr, field_validator

from core.utils.validators import validation_password_complexity


class UserRegistrationSchema(BaseModel):
    email: EmailStr
    password: str

    @field_validator('password')
    @classmethod
    def validate_password(cls, value: str) -> str:
        return validation_password_complexity(value)