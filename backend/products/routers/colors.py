from fastapi import APIRouter


colors_router = APIRouter(
    prefix='/colors',
    tags=['Colors'],
)