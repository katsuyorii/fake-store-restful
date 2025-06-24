from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.ext.asyncio import AsyncSession

from core.dependencies.database import get_db
from core.utils.jwt import verify_jwt_token
from core.utils.exceptions import UserNotFound

from .repositories import UsersRepository
from .models import UserModel


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_users_repository(db: AsyncSession = Depends(get_db)) -> UsersRepository:
    return UsersRepository(db)

async def get_current_user(access_token: str = Depends(oauth2_scheme), users_repository: UsersRepository = Depends(get_users_repository)) -> UserModel:
    payload = verify_jwt_token(access_token)

    user = await users_repository.get_by_id(int(payload.get('sub')))

    if not user or user.is_active:
        raise UserNotFound()

    return user