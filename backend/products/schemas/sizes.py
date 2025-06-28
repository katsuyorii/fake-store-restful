from pydantic import BaseModel


class SizeResponseSchema(BaseModel):
    id: int
    name: str


class SizeCreateSchema(BaseModel):
    name: str


class SizeUpdateSchema(BaseModel):
    name: str