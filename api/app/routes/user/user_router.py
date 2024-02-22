from typing import Iterable

from fastapi import APIRouter, Depends, HTTPException, status

from ...models.user import User
from ...schemas.auth_schemas import UserOut
from ...services.auth_service import authentication
from ...services.user_service import UserService

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get("/all")
async def get_all_user(
    user_service: UserService = Depends(UserService),
    current_user: User = Depends(authentication),
) -> Iterable[UserOut]:
    return user_service.find_all_user(current_user)
