from dataclasses import dataclass
from typing import Optional
import redis


@dataclass
class RedisConnection:
    pool: Optional[redis.ConnectionPool] = None
    client: Optional[redis.Redis] = None

    async def disconnect(self):
        if not self.client or not self.pool:
            return

        self.client.close()
        self.pool.disconnect()

    async def connect(self) -> None:
        try:
            self.pool = redis.ConnectionPool(host="127.0.0.1", port=6379)
            self.client = redis.Redis.from_pool(self.pool)

            response = self.client.ping()
            print(f"Connect to Redis: {response}")
        except Exception as exception:
            print(f"Failed to connect to Redis: {exception}")


redis_connection = RedisConnection()
