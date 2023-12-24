from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TT_API_URL: str
    model_config = SettingsConfigDict(env_file=".env")
