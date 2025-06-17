from fastapi import FastAPI
from app.api.endpoints import items, users # Import your endpoint routers
from app.core.config import settings
#from app.core.database import database # If using a database

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
)

# Include your API routers
app.include_router(items.router, prefix=settings.API_V1_STR, tags=["items"])
app.include_router(users.router, prefix=settings.API_V1_STR, tags=["users"])

# Database connection/disconnection events (if applicable)
#@app.on_event("startup")
#async def startup_event():
#    await database.connect()

#@app.on_event("shutdown")
#async def shutdown_event():
#    await database.disconnect()

# Basic root endpoint (optional)
@app.get("/")
async def read_root():
    return {"message": "Welcome to your FastAPI application!"}

# You would run this with `uvicorn app.main:app --reload`