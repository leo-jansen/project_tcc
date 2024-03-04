from typing import Iterable

from fastapi import Depends
from sqlalchemy.orm import Session

from ..config.database import get_db
from ..models.profile import Profile
from ..schemas.user_schemas import ProfileOut


class ProfileRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def find_by_id(self, id: int) -> Profile:
        return self.db.query(Profile).filter(Profile.profile_id == id).first()

    def get_all_profiles(self) -> Iterable[ProfileOut]:
        listProfile = self.db.query(Profile).filter(Profile.status == "S").all()
        return list(
            map(lambda x: ProfileOut(id=x.profile_id, name=x.profile_nm), listProfile)
        )
