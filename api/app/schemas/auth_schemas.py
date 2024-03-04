from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str


class TokenData(BaseModel):
    usr_login: str | None = None


class UserIn(BaseModel):
    username: str
    email: str
    name: str
    company: int
    profile: int


class UserOut(BaseModel):
    id: int
    username: str
    email: str
    name: str
    company: int
    profile: int


class AccessToken(BaseModel):
    access_token: str
    token_type: str
    user: UserOut
