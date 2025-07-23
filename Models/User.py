from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, BigInteger, String, Date, ForeignKey
from Models.Base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=True)

    role = relationship("Role", back_populates="users")
    user_claims = relationship("UserClaim", back_populates="user")
