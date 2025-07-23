from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, ForeignKey
from .Base import Base

class UserClaim(Base):
    __tablename__ = "user_claims"
    user_id = Column(BigInteger, ForeignKey("users.id"), primary_key=True)
    claim_id = Column(BigInteger, ForeignKey("claims.id"), primary_key=True)

    user = relationship("User", back_populates="user_claims")
    claim = relationship("Claim", back_populates="user_claims")