from redis.asyncio import Redis


class RedisBaseRepository:
    def __init__(self, redis: Redis):
        self.redis = redis
    
    async def set(self, key: str, value: str) -> None:
        await self.redis.set(key, value)
    
    async def setex(self, key: str, value: str, ex: int) -> None:
        await self.redis.set(key, value, ex)

    async def get(self, key: str) -> str | None:
        return await self.redis.get(key)
    
    async def delete(self, key: str) -> None:
        await self.redis.delete(key)
    
    async def exists(self, key: str) -> bool:
        return await self.exists(key) > 0