from fastapi import HTTPException, status


class EmailAlreadyRegistered(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail='Email is already registered')


class JWTTokenExpired(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token has expired')


class JWTTokenInvalid(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')