import os
import importlib
import pkgutil
from sqlalchemy import create_engine
from Models.Base import Base


def createTabels():
    database_url = os.getenv("DATABASE_URL")
    engine = create_engine(database_url)

    package = "Models"
    for _, name, _ in pkgutil.iter_modules([package]):
        if name != "base":
            importlib.import_module(f"{package}.{name}")

    Base.metadata.create_all(engine)
