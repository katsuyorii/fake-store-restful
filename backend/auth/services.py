from core.utils.exceptions import EmailAlreadyRegistered
from core.utils.password import hashing_password

from users.repositories import UsersRepository

from .schemas import UserRegistrationSchema


class AuthService:
    def __init__(self, users_repository: UsersRepository):
        self.users_repository = users_repository
    
    async def registration(self, user_data: UserRegistrationSchema) -> None:
        user = await self.users_repository.get_by_email(user_data.email)

        if user is not None:
            raise EmailAlreadyRegistered()
        
        user_data_dict = user_data.model_dump()
        user_data_dict['password'] = hashing_password(user_data.password)

        await self.users_repository.create(user_data_dict)