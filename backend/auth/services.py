from fastapi import Response, Request

from datetime import datetime, timedelta, timezone

from core.utils.exceptions import EmailAlreadyRegistered
from core.utils.password import hashing_password, verify_password
from core.utils.jwt import create_jwt_token

from src.settings import jwt_settings

from users.repositories import UsersRepository

from .schemas import AccessTokenSchema, UserRegistrationSchema, UserLoginSchema
from .exceptions import LoginOrPasswordIncorrect, AccountNotActive, TokenMissing


class TokensService:
    def __init__(self, access_token_minutes_expire: int = jwt_settings.ACCESS_TOKEN_MINUTES_EXPIRE, refresh_token_days_expire: int = jwt_settings.REFRESH_TOKEN_DAYS_EXPIRE):
        self.access_token_minutes_expire = access_token_minutes_expire
        self.refresh_token_days_expire = refresh_token_days_expire

    def create_access_token(self, payload: dict) -> str:
        to_encode = payload.copy()

        iat = datetime.now(timezone.utc)
        exp = iat + timedelta(minutes=self.access_token_minutes_expire)

        to_encode.update({'iat': iat, 'exp': exp})
        access_token = create_jwt_token(to_encode)

        return access_token
    
    def create_refresh_token(self, payload: dict) -> str:
        to_encode = payload.copy()

        iat = datetime.now(timezone.utc)
        exp = iat + timedelta(days=self.refresh_token_days_expire)
        
        to_encode.update({'iat': iat, 'exp': exp})
        refresh_token = create_jwt_token(to_encode)

        return refresh_token
    
    def set_token_to_cookies(self, response: Response, key: str, value: str, max_age: int) -> None:
        response.set_cookie(
            key=key,
            value=value,
            max_age=max_age,
            samesite='strict',
            secure=True,
            httponly=True,
        )


class AuthService:
    def __init__(self, users_repository: UsersRepository, tokens_service: TokensService):
        self.users_repository = users_repository
        self.tokens_service = tokens_service
    
    async def registration(self, user_data: UserRegistrationSchema) -> None:
        user = await self.users_repository.get_by_email(user_data.email)

        if user is not None:
            raise EmailAlreadyRegistered()
        
        user_data_dict = user_data.model_dump()
        user_data_dict['password'] = hashing_password(user_data.password)

        await self.users_repository.create(user_data_dict)
    
    async def authentication(self, user_data: UserLoginSchema, response: Response) -> AccessTokenSchema:
        user = await self.users_repository.get_by_email(user_data.email)

        if not user or not verify_password(user_data.password, user.password):
            raise LoginOrPasswordIncorrect()
        
        if user.is_active:
            raise AccountNotActive()
        
        access_token = self.tokens_service.create_access_token({'sub': str(user.id), 'role': user.role})
        refresh_token = self.tokens_service.create_refresh_token({'sub': str(user.id)})

        self.tokens_service.set_token_to_cookies(response, 'access_token', access_token, jwt_settings.ACCESS_TOKEN_MINUTES_EXPIRE * 60)
        self.tokens_service.set_token_to_cookies(response, 'refresh_token', refresh_token, jwt_settings.REFRESH_TOKEN_DAYS_EXPIRE * 24 * 60 * 60)

        return AccessTokenSchema(access_token=access_token)
    
    async def logout(self, request: Request, response: Response):
        access_token = request.cookies.get('access_token')

        if not access_token:
            raise TokenMissing()

        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')