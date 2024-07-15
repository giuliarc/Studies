import shutil
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from allocation.adapters.orm import metadata, start_mappers


@pytest.fixture
def in_memoty_sqlite_db():
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    return engine