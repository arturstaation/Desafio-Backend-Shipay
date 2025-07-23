import os
import importlib
import pkgutil
from sqlalchemy import create_engine
from Models.Base import Base


def createTabels():
    engine = create_engine("postgresql://postgres:123@localhost:5432/Teste")

    package = "Models"
    for _, name, _ in pkgutil.iter_modules([package]):
        if name != "base":
            importlib.import_module(f"{package}.{name}")

    Base.metadata.create_all(engine)
