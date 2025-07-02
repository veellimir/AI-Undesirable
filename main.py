import uvicorn

from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.settings import settings

# from api_v1 import router as api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # await create_superuser()
    yield
    # shutdown

app = FastAPI(
    title="🎩 API Сервис модерации.",
    description="Сервер, который принимает изображение и отправляет его в бесплатный сервис модерации ",
    lifespan=lifespan,
)

# app.include_router(api_router)


origins = [
    "http://localhost:5173",
]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
#     allow_headers=["Content-type", "Set-Cookie", "Access-Control-Allow-Headers", "Authorization"]
# )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
