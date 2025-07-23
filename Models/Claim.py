from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, String, Boolean
from Models.Base import Base

class Claim(Base):
    __tablename__ = "claims"
    id = Column(BigInteger, primary_key=True)
    description = Column(String, nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    user_claims = relationship("UserClaim", back_populates="claim")