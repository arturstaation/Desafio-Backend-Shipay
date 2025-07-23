from Models import User
import secrets
import random
from typing import Self, List
from datetime import datetime, timezone
from Repository import DatabaseRepository
from Utils import getLogger
import traceback


logger = getLogger(__name__)

class UserService:

    databaseRepository : DatabaseRepository

    def __init__(self : Self):
        try:
            self.databaseRepository = DatabaseRepository()
        except Exception as e:
            stacktrace = traceback.format_exc() 
            logger.error(f"Erro ao criar instancia para acessar o banco de dados. Erro: {str(e)}. Stacktrace: {stacktrace}")

    def createUser(self: Self, userData: User) -> User:
        
        logger.info(f"Verificando se a role {userData.role_id} existe")
        self.databaseRepository.getRoleById(userData.role_id)
        if(userData.password == None):
            logger.debug(f"Gerando senha")
            userData.password = secrets.token_urlsafe(random.randint(8,32))
        userData.created_at = datetime.now(timezone.utc)
        userData.updated_at = datetime.now(timezone.utc)
        return self.databaseRepository.createUser(userData)
    
    def getRoles(self: Self, userId: int) -> List[int]:
        return self.databaseRepository.getUserRoles(userId)
