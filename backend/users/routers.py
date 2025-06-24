from fastapi import APIRouter, Depends, status

from .schemas import UserResponseSchema, UserUpdateSchema
from .services import UsersService
from .dependencies import get_users_service


users_router = APIRouter(
    prefix='/users',
    tags=['Users'],
)

@users_router.get('/me', response_model=UserResponseSchema)
async def get_me(users_service: UsersService = Depends(get_users_service)):
    return await users_service.get_me()

@users_router.patch('/me', response_model=UserResponseSchema)
async def update_me(user_updated_data: UserUpdateSchema, users_service: UsersService = Depends(get_users_service)):
    return await users_service.update_me(user_updated_data)

@users_router.delete('/me', status_code=status.HTTP_204_NO_CONTENT)
async def delete_me(users_service: UsersService = Depends(get_users_service)):
    await users_service.delete_me()