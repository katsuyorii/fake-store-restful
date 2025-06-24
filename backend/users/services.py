from .repositories import UsersRepository, UsersAddressesRepository
from .models import UserModel
from .schemas import UserUpdateSchema


class UsersAddressesService:
    def __init__(self, current_user: UserModel, users_addresses_repository: UsersAddressesRepository):
        self.current_user = current_user
        self.users_addresses_repository = users_addresses_repository


class UsersService:
    def __init__(self, current_user: UserModel, users_repository: UsersRepository):
        self.current_user = current_user
        self.users_repository = users_repository
    
    async def get_me(self) -> UserModel:
        return self.current_user
    
    async def update_me(self, user_updated_data: UserUpdateSchema) -> UserModel:
        updated_user = await self.users_repository.update(self.current_user, user_updated_data.model_dump(exclude_unset=True))

        return updated_user
    
    async def delete_me(self) -> None:
        await self.users_repository.delete(self.current_user)