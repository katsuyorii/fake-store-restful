from fastapi import APIRouter


brands_router = APIRouter(
    prefix='/brands',
    tags=['Brands'],
)