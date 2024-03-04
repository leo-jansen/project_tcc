from pydantic import BaseModel


class ProfileOut(BaseModel):
    id: int
    name: str


class CompanyOut(BaseModel):
    id: int
    name: str
