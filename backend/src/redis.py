from redis.asyncio import Redis, ConnectionPool

from .settings import redis_settings


redis_pool = ConnectionPool(
    host=redis_settings.REDIS_HOST,
    port=redis_settings.REDIS_PORT,
    password=redis_settings.REDIS_PASSWORD,
    max_connections=redis_settings.REDIS_MAX_CONNECTIONS,
)

redis_client = Redis(connection_pool=redis_pool)