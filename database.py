import asyncpg

from config import DB_DSN


class Database:
    def __init__(self, pool=None):
        self.pool = pool

    async def connect(self):
        self.pool = await asyncpg.create_pool(DB_DSN)

    async def disconnect(self):
        await self.pool.close()

    async def execute(self, query, *args):
        async with self.pool.acquire() as connection:
            return await connection.execute(query, *args)
