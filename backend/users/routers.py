from fastapi import APIRouter, Depends, status

from .schemas import UserResponseSchema, UserUpdateSchema, UserAddressResponseSchema, UserAddressCreateSchema, UserAddressUpdateSchema
from .services import UsersService, UsersAddressesService
from .dependencies import get_users_service, get_users_addresses_service


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

@users_router.get('/me/addresses', response_model=list[UserAddressResponseSchema])
async def get_all_addresses(skip: int | None = None, limit: int | None = None, users_addresses_service: UsersAddressesService = Depends(get_users_addresses_service)):
    return await users_addresses_service.get_all_addresses(skip, limit)

@users_router.get('/me/addresses/{address_id}', response_model=UserAddressResponseSchema)
async def get_address(address_id: int, users_addresses_service: UsersAddressesService = Depends(get_users_addresses_service)):
    return await users_addresses_service.get_address(address_id)

@users_router.post('/me/addresses', status_code=status.HTTP_201_CREATED, response_model=UserAddressResponseSchema)
async def create_address(address_data: UserAddressCreateSchema, users_addresses_service: UsersAddressesService = Depends(get_users_addresses_service)):
    return await users_addresses_service.create_address(address_data)

@users_router.patch('/me/addresses/{address_id}', response_model=UserAddressResponseSchema)
async def update_address(address_id: int, address_updated_data: UserAddressUpdateSchema, users_addresses_service: UsersAddressesService = Depends(get_users_addresses_service)):
    return await users_addresses_service.update_address(address_id, address_updated_data)

@users_router.delete('/me/addresses/{address_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_address(address_id: int, users_addresses_service: UsersAddressesService = Depends(get_users_addresses_service)):
    await users_addresses_service.delete_address(address_id)