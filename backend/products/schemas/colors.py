from pydantic import BaseModel


class ColorResponseSchema(BaseModel):
    id: int
    name: str


class ColorCreateSchema(BaseModel):
    name: str


class ColorUpdateSchema(BaseModel):
    name: str