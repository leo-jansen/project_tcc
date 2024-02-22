from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str


class TokenData(BaseModel):
    usr_login: str | None = None


class UserIn(BaseModel):
    username: str
    password: str
    email: str
    name: str
    company_id: int
    profile_id: int


class UserOut(BaseModel):
    username: str
    email: str
    name: str
    company: str
    profile: str


class AccessToken(BaseModel):
    access_token: str
    token_type: str
    user: UserOut
