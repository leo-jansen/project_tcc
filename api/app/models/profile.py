import uuid

from sqlalchemy import CHAR, Column, Integer, String, Text
from sqlalchemy.orm import relationship

from ..config.database import Base


class Profile(Base):
    __tablename__ = "Profile"
    __table_args__ = {"schema": "CONTROL"}

    profile_id = Column(Integer, primary_key=True, autoincrement=True)
    profile_nm = Column(String(100), nullable=True)
    status = Column(CHAR(1), nullable=True)
    obs = Column(Text, nullable=True)
