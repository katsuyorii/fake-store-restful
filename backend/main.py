from fastapi import FastAPI

from auth.routers import auth_router
from users.routers import users_router
from products.routers.products import products_router
from products.routers.categories import categories_router
from products.routers.brands import brands_router
from products.routers.sizes import sizes_router
from products.routers.colors import colors_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(products_router)
app.include_router(categories_router)
app.include_router(brands_router)
app.include_router(sizes_router)
app.include_router(colors_router)