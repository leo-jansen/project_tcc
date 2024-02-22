import uuid

from sqlalchemy import CHAR, Column, Integer, String
from sqlalchemy.orm import relationship

from ..config.database import Base


class Company(Base):
    __tablename__ = "Company"
    __table_args__ = {"schema": "CONTROL"}

    id_company = Column(Integer, primary_key=True, autoincrement=True)
    nm_company = Column(String(100), nullable=False)
    status = Column(CHAR(1), nullable=False)
