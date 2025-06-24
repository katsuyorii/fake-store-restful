from fastapi import FastAPI

from auth.routers import auth_router
from users.routers import users_router
from products.routers import products_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(products_router)