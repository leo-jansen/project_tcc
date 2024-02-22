from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from ...models.user import User
from ...schemas.auth_schemas import AccessToken, UserIn, UserLogin, UserOut
from ...services.auth_service import AuthService, authentication

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/singin")
async def login(
    data: UserLogin, service: AuthService = Depends(AuthService)
) -> AccessToken:
    accessToken = service.login(data.username, data.password)
    return accessToken


@router.post("/singup", status_code=status.HTTP_201_CREATED)
async def create_user(
    data: UserIn,
    service: AuthService = Depends(AuthService),
    current_user: User = Depends(authentication),
) -> UserOut:
    try:
        user_out = service.create_user(data, current_user)
        return user_out
    except Exception as e:
        raise HTTPException(status_code=500, detail=e._message)
