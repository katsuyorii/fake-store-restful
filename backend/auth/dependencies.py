from fastapi import Depends

from users.repositories import UsersRepository
from users.dependencies import get_users_repository

from .services import AuthService, TokensService


def get_tokens_service() -> TokensService:
    return TokensService()

def get_auth_service(users_repository: UsersRepository = Depends(get_users_repository), tokens_service: TokensService = Depends(get_tokens_service)) -> AuthService:
    return AuthService(users_repository, tokens_service)