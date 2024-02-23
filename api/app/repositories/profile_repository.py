from typing import Iterable

from fastapi import Depends
from sqlalchemy.orm import Session

from ..config.database import get_db
from ..models.profile import Profile


class ProfileRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def find_by_id(self, id: int) -> Profile:
        return self.db.query(Profile).filter(Profile.profile_id == id).first()
