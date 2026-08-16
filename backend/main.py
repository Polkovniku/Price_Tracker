from fastapi import FastAPI
from app.routers.users import router as user_router
from app.routers.products import router as product_router
from app.routers.auth import router as auth_router
from contextlib import asynccontextmanager
from camoufox.async_api import AsyncCamoufox


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncCamoufox(headless=True) as browser:
        page = await browser.new_page()
        app.state.page = page
        yield

app = FastAPI(lifespan=lifespan)

app.include_router(user_router)
app.include_router(product_router)
app.include_router(auth_router)