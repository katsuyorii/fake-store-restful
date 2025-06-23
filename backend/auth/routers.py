from fastapi import APIRouter, Response, Request, Depends, status

from .schemas import AccessTokenSchema, UserRegistrationSchema, UserLoginSchema
from .services import AuthService
from .dependencies import get_auth_service


auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth'],
)


@auth_router.post('/registration', status_code=status.HTTP_201_CREATED)
async def registration_user(user_data: UserRegistrationSchema, auth_service: AuthService = Depends(get_auth_service)):
    await auth_service.registration(user_data)
    return {'message': 'A confirmation letter has been sent to your email!'}

@auth_router.post('/login', response_model=AccessTokenSchema)
async def login_user(user_data: UserLoginSchema, response: Response, auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.authentication(user_data, response)

@auth_router.post('/logout')
async def logout_user(request: Request, response: Response, auth_service: AuthService = Depends(get_auth_service)):
    await auth_service.logout(request, response)
    return {'message': 'You have successfully logged!'}