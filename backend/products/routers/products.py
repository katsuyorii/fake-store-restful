from fastapi import APIRouter


products_router = APIRouter(
    prefix='/products',
    tags=['Products'],
)