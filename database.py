from databases import Database
from sqlalchemy import (
    MetaData,
    create_engine,
    Table,
    Column,
    Integer,
    String,
    DateTime,
    func,
    Identity
)



DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"
# DATABASE_URL = "postgresql://codegirl:password@localhost:5432/database1"

database = Database(DATABASE_URL)
metadata = MetaData()


posts = Table(
    'posts',
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column("author", String),
    Column("text", String),
    Column("keywords", String),
    Column("created_at", DateTime, server_default=func.now())
)

engine = create_engine(DATABASE_URL)

metadata.create_all(engine)
