from datetime import datetime
from typing import Iterable

from fastapi import Depends
from sqlalchemy.orm import Session

from ..config.database import get_db
from ..models.user import User
from ..schemas.auth_schemas import UserOut


class UserRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def find_by_usr_nm(self, name: str) -> User:
        return self.db.query(User).filter(User.usr_nm == name).first()

    def find_by_usr_email(self, email: str) -> User:
        return self.db.query(User).filter(User.usr_email == email).first()

    def find_by_usr_login(self, usr_login: str) -> User:
        return self.db.query(User).filter(User.usr_login == usr_login).first()

    def find_all_by_profile(self, profile_id: int):
        list_user = self.db.query(User).filter(User.profile_id == profile_id).all()
        return list(
            map(
                lambda x: UserOut(
                    username=x.usr_login,
                    email=x.usr_email,
                    name=x.usr_nm,
                    company=x.company.nm_company if x.company else "",
                    profile=x.profile.profile_nm if x.profile else "",
                ),
                list_user,
            )
        )

    def find_all_by_company(self, company_id: int):
        list_user = self.db.query(User).filter(User.id_company == company_id).all()
        return list(
            map(
                lambda x: UserOut(
                    username=x.usr_login,
                    email=x.usr_email,
                    name=x.usr_nm,
                    company=x.company.nm_company if x.company else "",
                    profile=x.profile.profile_nm if x.profile else "",
                ),
                list_user,
            )
        )

    def find_all(self) -> Iterable[UserOut]:
        list_user = self.db.query(User).all()
        return list(
            map(
                lambda x: UserOut(
                    username=x.usr_login,
                    email=x.usr_email,
                    name=x.usr_nm,
                    company=x.company.nm_company if x.company else "",
                    profile=x.profile.profile_nm if x.profile else "",
                ),
                list_user,
            )
        )

    def update_last_login(self, user: User) -> User:
        user.last_login = datetime.now()
        self.db.commit()
        return user

    def save(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
