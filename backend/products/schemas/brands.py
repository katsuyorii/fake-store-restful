from pydantic import BaseModel


class BrandResponseSchema(BaseModel):
    id: int
    name: str
    slug: str


class BrandCreateSchema(BaseModel):
    name: str


class BrandUpdateSchema(BaseModel):
    name: str