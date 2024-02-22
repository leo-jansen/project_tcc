from typing import Iterable

from fastapi import Depends

from ..models.user import User
from ..repositories.user_repository import UserRepository
from ..schemas.auth_schemas import UserOut


class UserService:
    user_repository: UserRepository

    def __init__(
        self, user_repository: UserRepository = Depends(UserRepository)
    ) -> None:
        self.user_repository = user_repository
        pass

    def find_all_user(self, current_user: User) -> Iterable[UserOut]:
        if current_user.profile_id == 1:
            return self.user_repository.find_all()
        else:
            return self.user_repository.find_all_by_company(current_user.id_company)
