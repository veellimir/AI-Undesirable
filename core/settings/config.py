from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiV1Prefix(BaseModel):
    prefix: str = "/api/v1"

    moderation: str = "/moderation"


class ApiPrefix(BaseModel):
    v1: ApiV1Prefix = ApiV1Prefix()


class Settings(BaseSettings):
    SECRET_KEY: str

    DEEPAI_URL: str
    DEEPAI_KEY: str

    api: ApiPrefix = ApiPrefix()
    run: RunConfig = RunConfig()

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",
    )


settings = Settings()
