from fastapi import FastAPI

from auth.routers import auth_router
from users.routers import users_router
from products.routers import products_router, categories_router, brands_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(products_router)
app.include_router(categories_router)
app.include_router(brands_router)