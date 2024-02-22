from sqlalchemy import CHAR, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from ..config.database import Base
from .company import Company
from .profile import Profile


class User(Base):
    __tablename__ = "UsrData"
    __table_args__ = {"schema": "CONTROL"}

    usr_id = Column(Integer, primary_key=True, autoincrement=True)
    usr_nm = Column(String(200), nullable=True)
    usr_pwd = Column(Text, nullable=True)
    profile_id = Column(Integer, ForeignKey("CONTROL.Profile.profile_id"))
    id_company = Column(Integer, ForeignKey("CONTROL.Company.id_company"))
    usr_login = Column(String(200), nullable=True)
    usr_email = Column(String(200), nullable=True)
    usr_status = Column(CHAR(1), nullable=True)
    last_login = Column(DateTime, nullable=True)
    last_page = Column(Text, nullable=True)

    company = relationship("Company")
    profile = relationship("Profile")
