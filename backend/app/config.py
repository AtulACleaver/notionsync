from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra = "ignore")
    DATABASE_URL: str
    NOTION_TOKEN: str = ""
    NOTION_WEBHOOK_SECRET: str = ""
    NOTION_POSTS_DATABASE_ID: str = ""
    NOTION_TEMPLATES_DATABASE_ID: str = ""
    APP_ENV: str = "development"
    CORS_ORIGINS: str = "http://localhost:5173"

settings = Settings()
