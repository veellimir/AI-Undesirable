from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiV1Prefix(BaseModel):
    prefix: str = "/api/v1"


class ApiPrefix(BaseModel):
    v1: ApiV1Prefix = ApiV1Prefix()


class ApiSecretKey(BaseSettings):
    pass


class Settings(BaseSettings):
    SECRET_KEY: str

    api_key: ApiSecretKey = ApiSecretKey()

    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"


settings = Settings()
