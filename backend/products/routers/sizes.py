from fastapi import APIRouter


sizes_router = APIRouter(
    prefix='/sizes',
    tags=['Sizes'],
)