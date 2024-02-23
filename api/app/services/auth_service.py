from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from ..models.user import User
from ..repositories.company_repository import CompanyRepository
from ..repositories.profile_repository import ProfileRepository
from ..repositories.user_repository import UserRepository
from ..schemas.auth_schemas import AccessToken, TokenData, UserIn, UserOut
from ..util.consts import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authentication(
    user_repository: Annotated[UserRepository, Depends(UserRepository)],
    token: Annotated[str, Depends(oauth2_scheme)],
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usr_login: str = payload.get("sub")
        if usr_login is None:
            raise credentials_exception
        token_data = TokenData(usr_login=usr_login)
    except JWTError:
        raise credentials_exception

    user = user_repository.find_by_usr_login(token_data.usr_login)
    if user is None:
        raise credentials_exception

    if user.usr_status != "S":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario está desabilitado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


class AuthService:
    user_repository: UserRepository
    company_repository: CompanyRepository
    profile_repository: ProfileRepository

    def __init__(
        self,
        user_repository: UserRepository = Depends(UserRepository),
        company_repository: CompanyRepository = Depends(CompanyRepository),
        profile_repository: ProfileRepository = Depends(ProfileRepository),
    ) -> None:
        self.user_repository = user_repository
        self.company_repository = company_repository
        self.profile_repository = profile_repository
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        pass

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def login(self, username: str, password: str) -> AccessToken:
        user = self.user_repository.find_by_usr_login(username)
        if user is None:
            raise HTTPException(status_code=401, detail="Usuário e/ou senha inválidos")

        if not self.verify_password(password, user.usr_pwd):
            raise HTTPException(status_code=401, detail="Usuário e/ou senha inválidos")

        access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
        token = self.create_access_token(
            data={"sub": user.usr_login}, expires_delta=access_token_expires
        )
        self.user_repository.update_last_login(user)

        return {
            "access_token": token,
            "token_type": "bearer",
            "user": {
                "username": user.usr_login,
                "email": user.usr_email,
                "name": user.usr_nm,
                "company": user.company.nm_company,
                "profile": user.profile.profile_nm,
            },
        }

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def create_user(self, user_create: UserIn, current_user: User) -> UserOut:
        if current_user.profile_id == 1:
            user = User()
            user.usr_login = user_create.username
            user.usr_pwd = self.get_password_hash(user_create.password)
            user.usr_email = user_create.email
            user.usr_nm = user_create.name
            user.usr_status = "S"
            user.id_company = user_create.company_id
            user.profile_id = user_create.profile_id
            self.user_repository.save(user)

            company = self.company_repository.find_by_id(user_create.company_id)
            profile = self.profile_repository.find_by_id(user_create.profile_id)

            return UserOut(
                username=user_create.username,
                email=user_create.email,
                name=user_create.name,
                company=company.nm_company,
                profile=profile.profile_nm,
            )
        elif (
            current_user.profile_id == user_create.profile_id
            and current_user.id_company == user_create.company_id
            and current_user.profile_id != 3
        ):
            user = User()
            user.usr_login = user_create.username
            user.usr_pwd = self.get_password_hash(user_create.password)
            user.usr_email = user_create.email
            user.usr_nm = user_create.name
            user.usr_status = "S"
            user.id_company = user_create.company_id
            user.profile_id = user_create.profile_id
            self.user_repository.save(user)

            company = self.company_repository.find_by_id(user_create.company_id)
            profile = self.profile_repository.find_by_id(user_create.profile_id)

            return UserOut(
                username=user_create.username,
                email=user_create.email,
                name=user_create.name,
                company=company.nm_company,
                profile=profile.profile_nm,
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Usuario sem permissão apara essa ação",
            )
