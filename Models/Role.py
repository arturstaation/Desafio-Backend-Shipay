from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from Models.Base import Base

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    users = relationship("User", back_populates="role")