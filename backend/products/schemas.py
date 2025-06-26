from pydantic import BaseModel


class CategoryResponseSchema(BaseModel):
    id: int
    name: str
    slug: str


class CategoryCreateSchema(BaseModel):
    name: str