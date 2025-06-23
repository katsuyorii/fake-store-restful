import jwt

from src.settings import jwt_settings

from .exceptions import JWTTokenExpired, JWTTokenInvalid


def create_jwt_token(payload: dict) -> str:
    jwt_token = jwt.encode(
        payload=payload,
        key=jwt_settings.JWT_PRIVATE_KEY,
        algorithm=jwt_settings.JWT_ALGORITHM,
    )

    return jwt_token

def verify_jwt_token(jwt_token: str) -> dict:
    try:
        payload = jwt.decode(
            jwt=jwt_token,
            key=jwt_settings.JWT_PUBLIC_KEY,
            algorithms=[jwt_settings.JWT_ALGORITHM],
        )
    except jwt.ExpiredSignatureError:
        raise JWTTokenExpired()
    except jwt.InvalidTokenError:
        raise JWTTokenInvalid()
    
    return payload