from Models import User
from typing import Self
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import traceback
from typing import List
from Models import Base

DATABASE_URL = "postgresql://postgres:123@localhost:5432/Teste"

class DatabaseRepository:

    def __init__(self: Self):
        try:
            engine = create_engine(DATABASE_URL)
            Base.metadata.create_all(engine)
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            self.session = SessionLocal()
        except Exception as e:
            stacktrace = traceback.format_exc() 
            print(f"Ocorreu um erro durante a criação de sessão com o banco. Erro: {e}. Stacktrace: {stacktrace}")
            raise e


    def createUser(self: Self, user: User) -> User | None:
        try:
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
            return user
        except Exception as e:
            stacktrace = traceback.format_exc() 
            print(f"Ocorreu um erro durante a inserção de um novo usuario no banco. Erro: {e}. Stacktrace: {stacktrace}")
            self.session.rollback()
            raise e
        finally:
            self.session.close()

    def getRoles(self: Self, userId: int) -> List[int] | None:
        try:
            roles = self.session.query(User).filter(User.id == userId).all()
            role_ids = [user.role_id for user in roles]
            return role_ids
        except Exception as e:
            stacktrace = traceback.format_exc() 
            print(f"Ocorreu um erro durante a obtenção das roles de um usuario no banco. Erro: {e}. Stacktrace: {stacktrace}")
            self.session.rollback()
            raise e
        finally:
            self.session.close()