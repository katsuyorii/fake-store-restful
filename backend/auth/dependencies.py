from fastapi import Depends

from core.repositories.redis_base import RedisBaseRepository
from core.dependencies.redis import get_redis_repository

from users.repositories import UsersRepository
from users.dependencies import get_users_repository

from .services import AuthService, TokensService


def get_tokens_service() -> TokensService:
    return TokensService()

def get_auth_service(users_repository: UsersRepository = Depends(get_users_repository), tokens_service: TokensService = Depends(get_tokens_service), redis_repository: RedisBaseRepository = Depends(get_redis_repository)) -> AuthService:
    return AuthService(users_repository, tokens_service, redis_repository)