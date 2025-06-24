from .repositories import UsersRepository, UsersAddressesRepository
from .models import UserModel, UserAddressModel
from .schemas import UserUpdateSchema, UserAddressCreateSchema, UserAddressUpdateSchema
from .exceptions import AddressNotFound


class UsersAddressesService:
    def __init__(self, current_user: UserModel, users_addresses_repository: UsersAddressesRepository):
        self.current_user = current_user
        self.users_addresses_repository = users_addresses_repository
    
    async def get_all_addresses(self, skip: int | None = None, limit: int | None = None) -> list[UserAddressModel]:
        addresses = await self.users_addresses_repository.get_all(self.current_user.id, skip, limit)

        return addresses
    
    async def get_address(self, address_id: int) -> UserAddressModel | None:
        address = await self.users_addresses_repository.get_by_id(self.current_user.id, address_id)

        if not address:
            raise AddressNotFound()
        
        return address
    
    async def create_address(self, address_data: UserAddressCreateSchema) -> UserAddressModel:
        address_data_dict = address_data.model_dump(exclude_unset=True)
        address_data_dict['user_id'] = self.current_user.id

        new_address = await self.users_addresses_repository.create(address_data_dict)

        return new_address
    
    async def update_address(self, address_id: int, address_updated_data: UserAddressUpdateSchema) -> UserAddressModel | None:
        address = await self.users_addresses_repository.get_by_id(self.current_user.id, address_id)

        if not address:
            raise AddressNotFound()
        
        await self.users_addresses_repository.update(address, address_updated_data.model_dump(exclude_unset=True))

        return address
    
    async def delete_address(self, address_id: int) -> None:
        address = await self.users_addresses_repository.get_by_id(self.current_user.id, address_id)

        if not address:
            raise AddressNotFound()
        
        await self.users_addresses_repository.delete(address)


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