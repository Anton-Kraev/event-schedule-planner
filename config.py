from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TT_API_URL: HttpUrl
    model_config = SettingsConfigDict(env_file=".env")
