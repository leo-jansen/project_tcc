from typing import Iterable

from fastapi import Depends
from sqlalchemy.orm import Session

from ..config.database import get_db
from ..models.company import Company
from ..schemas.user_schemas import CompanyOut


class CompanyRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def find_by_id(self, id: int) -> Company:
        return self.db.query(Company).filter(Company.id_company == id).first()

    def get_all_companies(self) -> Iterable[CompanyOut]:
        list_companies = self.db.query(Company).filter(Company.status == "S").all()
        return list(
            map(
                lambda x: CompanyOut(id=x.id_company, name=x.nm_company), list_companies
            )
        )
