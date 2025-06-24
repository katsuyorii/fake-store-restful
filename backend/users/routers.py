from fastapi import APIRouter, Depends

from .schemas import UserResponseSchema
from .models import UserModel
from .dependencies import get_current_user


users_router = APIRouter(
    prefix='/users',
    tags=['Users'],
)

@users_router.get('/me', response_model=UserResponseSchema)
async def get_me(user: UserModel = Depends(get_current_user)):
    return user