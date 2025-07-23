from typing import Self
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import traceback
from typing import List
from Models import Base, User, Role
import os
from Utils import getLogger

logger = getLogger(__name__)
class DatabaseRepository:

    def __init__(self: Self):
        try:
            
            logger.info(f"Criando conexão com o banco de dados")
            database_url = os.getenv("DATABASE_URL")
            engine = create_engine(database_url)
            Base.metadata.create_all(engine)
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            self.session = SessionLocal()
            logger.info(f"Conexão com o banco estabelecida")
        except Exception as e:
            stacktrace = traceback.format_exc() 
            logger.error(f"Ocorreu um erro durante a criação de sessão com o banco. Erro: {e}. Stacktrace: {stacktrace}")
            raise e


    def createUser(self: Self, user: User) -> User | None:
        try:
            logger.info(f"Adicionando usuario ao banco de dados")
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
            return user
        except Exception as e:
            stacktrace = traceback.format_exc() 
            logger.error(f"Ocorreu um erro durante a inserção de um novo usuario no banco. Erro: {e}. Stacktrace: {stacktrace}")
            self.session.rollback()
            raise e
        finally:
            logger.info(f"Fechando sessão com o banco de dados")
            self.session.close()

    def getUserRoles(self: Self, userId: int) -> List[int] | None:
        try:
            logger.info(f"Obtendo roles para o usuario {userId}")
            roles = self.session.query(User).filter(User.id == userId).all()
            role_ids = [user.role_id for user in roles]
            return role_ids
        except Exception as e:
            stacktrace = traceback.format_exc() 
            logger.error(f"Ocorreu um erro durante a obtenção das roles de um usuario no banco. Erro: {e}. Stacktrace: {stacktrace}")
            self.session.rollback()
            raise e
        finally:
            logger.info(f"Fechando sessão com o banco de dados")
            self.session.close()

    def getRoleById(self: Self, roleId: int):
        role = self.session.query(Role).filter(Role.id == roleId).first()
        if not role:
            raise ValueError(f"O role_id {roleId} não existe.")