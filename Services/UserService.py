from Models import User
import secrets
import random
from typing import Self, List
from datetime import datetime, timezone
from Repository import DatabaseRepository

class UserService:

    databaseRepository : DatabaseRepository

    def __init__(self : Self):
        try:
            self.databaseRepository = DatabaseRepository()
        except Exception as e:
            print()


    def createUser(self: Self, userData: User) -> User:
        if(userData.password == None):
            userData.password = secrets.token_urlsafe(random.randint(8,32))
        userData.created_at = datetime.now(timezone.utc)
        userData.updated_at = datetime.now(timezone.utc)
        return self.databaseRepository.createUser(userData)
    
    def getRoles(self: Self, userId: int) -> List[int]:
        return self.databaseRepository.getRoles(userId)
