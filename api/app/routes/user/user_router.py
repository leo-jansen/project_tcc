from typing import Iterable

from fastapi import APIRouter, Depends, HTTPException, status

from ...models.user import User
from ...schemas.auth_schemas import UserOut
from ...schemas.user_schemas import CompanyOut, ProfileOut
from ...services.auth_service import authentication
from ...services.user_service import UserService

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.put("/{id}")
async def update_user(
    id: int,
    data: UserIn,
    user_service: UserService = Depends(UserService),
    current_user: User = Depends(authentication),
) -> UserOut:
    return user_service.update_user(id, data, current_user)


@router.get("/all")
async def get_all_user(
    user_service: UserService = Depends(UserService),
    current_user: User = Depends(authentication),
) -> Iterable[UserOut]:
    return user_service.find_all_user(current_user)


@router.get("/profile")
async def get_user_profiles(
    user_service: UserService = Depends(UserService),
    current_user: User = Depends(authentication),
) -> Iterable[ProfileOut]:
    return user_service.get_user_profiles(current_user)


@router.get("/company")
async def get_user_companies(
    user_service: UserService = Depends(UserService),
    current_user: User = Depends(authentication),
) -> Iterable[CompanyOut]:
    return user_service.get_user_companies(current_user)
