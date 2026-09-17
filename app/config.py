from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Task Manager API"
    database_url: str = "sqlite:///./test.db"
    secret_key: str

    model_config = {"env_file": ".env"}


settings = Settings()