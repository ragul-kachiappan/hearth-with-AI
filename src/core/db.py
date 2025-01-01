from contextlib import asynccontextmanager
from typing import AsyncGenerator

import asyncpg
from asyncpg.pool import Pool

from src.app.config import Settings


class Database:
    def __init__(self, settings: Settings):
        self.settings = settings
        self._pool: Pool | None = None

    async def connect(self) -> None:
        if not self._pool:
            self._pool = await asyncpg.create_pool(
                dsn=self.settings.database_url,
                min_size=2,
                max_size=10,
                command_timeout=60,
            )

    async def disconnect(self) -> None:
        if self._pool:
            await self._pool.close()
            self._pool = None

    @asynccontextmanager
    async def connection(self) -> AsyncGenerator[asyncpg.Connection, None]:
        if not self._pool:
            await self.connect()
        async with self._pool.acquire() as conn:
            yield conn


db = Database(Settings())


# @app.on_event("startup")
# async def startup():
#     await db.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await db.disconnect()

# # Usage example
# async def get_user(user_id: int):
#     async with db.connection() as conn:
#         return await conn.fetchrow(
#             "SELECT * FROM users WHERE id = $1",
#             user_id
#         )
