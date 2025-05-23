from core.configs import settings
from core.database import async_engine
from models import models

async def create_table() -> None:
    print("Criando as tabelas do banco de dados para The Last of Us")
    async with async_engine.begin() as conn:
        # Dropping existing tables if necessary
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        # Creating new tables with thematic names and structures
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print("Tabelas criadas com sucesso para The Last of Us")

if __name__ == "__main__":
    import asyncio
    asyncio.run(create_table())