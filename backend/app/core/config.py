from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import find_dotenv
from pydantic import BaseModel

class RedisDB(BaseModel):
    celery: int = 0

class RedisConfig(BaseModel):
    host: str = "redis"
    port: int = 6379
    db: RedisDB = RedisDB()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=find_dotenv())
    
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    SECRET_KEY: str
    redis: RedisConfig = RedisConfig()
    
    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}"
    
    @property
    def redis_url(self):
        return f"redis://{self.redis.host}:{self.redis.port}/{self.redis.db.celery}"
    
    
settings = Settings()