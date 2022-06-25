import aiosqlite
import os
import logging
from pathlib import Path

log = logging.getLogger(__name__)

class Database:
    __slots__ = ('sql_path', 'db_path', 'cxn')

    def __init__(self, dynamic: Path, static: Path) -> None:
        self.sql_path = (static / 'build.sql').resolve()
        self.db_path = (dynamic / 'database.db').resolve()

    async def connect(self) -> aiosqlite.Connection:
        self.cxn = await aiosqlite.connect(self.db_path)
        await self.cxn.executescript(self.sql_path.read_text())
        await self.cxn.commit()
        return self.cxn

    async def commit(self) -> None:
        await self.cxn.commit()

    async def close(self) -> None:
        await self.cxn.close()

    async def execute(self, query: str, *args) -> None:
        try:
            await self.cxn.execute(query, args)
        except Exception as e:
            log.error(f"❌  {e}")
            raise e

    async def fetchall(self, query: str, *args) -> list:
        try:
            return await self.cxn.execute(query, args).fetchall()
        except Exception as e:
            log.error(f"❌  {e}")
            raise e

    async def fetchone(self, query: str, *args) -> tuple:
        try:
            return await self.cxn.execute(query, args).fetchone()
        except Exception as e:
            log.error(f"❌  {e}")
            raise e

    