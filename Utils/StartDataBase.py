import os
import importlib
import pkgutil
from sqlalchemy import create_engine
from Models.Base import Base
from .Logger import getLogger

logger = getLogger(__name__)

def createTabels():
    try:
        logger.debug("Criando conexão com o banco")
        database_url = os.getenv("DATABASE_URL")
        engine = create_engine(database_url)

        
        logger.debug("Validando existencia das tabelas")
        package = "Models"
        for _, name, _ in pkgutil.iter_modules([package]):
            if name != "base":
                importlib.import_module(f"{package}.{name}")
        
        logger.debug("Criando tableas inexistentes")
        Base.metadata.create_all(engine)
    except Exception as e:
        logger.error(f"Erro ao validar e criar tabelas mapeadas. Erro {str(e)}. Stacktrace:")
        os._exit(0)
