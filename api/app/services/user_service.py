from typing import Iterable

from fastapi import Depends

from ..models.user import User
from ..repositories.company_repository import CompanyRepository
from ..repositories.profile_repository import ProfileRepository
from ..repositories.user_repository import UserRepository
from ..schemas.auth_schemas import UserIn, UserOut
from ..schemas.user_schemas import CompanyOut, ProfileOut


class UserService:
    user_repository: UserRepository
    profile_repository: ProfileRepository
    company_repository: CompanyRepository

    def __init__(
        self,
        user_repository: UserRepository = Depends(UserRepository),
        profile_repository: ProfileRepository = Depends(ProfileRepository),
        company_repository: ProfileRepository = Depends(CompanyRepository),
    ) -> None:
        self.user_repository = user_repository
        self.profile_repository = profile_repository
        self.company_repository = company_repository
        pass

    def find_all_user(self, current_user: User) -> Iterable[UserOut]:
        if current_user.profile_id == 1:
            return self.user_repository.find_all()
        else:
            return self.user_repository.find_all_by_company(current_user.id_company)

    def get_user_profiles(self, current_user: User) -> Iterable[ProfileOut]:
        list_profiles = self.profile_repository.get_all_profiles()
        if current_user.profile_id != 1:
            return list(filter(lambda profile: profile.id != 1, list_profiles))
        return list_profiles

    def get_user_companies(self, current_user: User) -> Iterable[CompanyOut]:
        list_companies = self.company_repository.get_all_companies()
        if current_user.profile_id != 1:
            return list(
                filter(
                    lambda company: company.id == current_user.id_company,
                    list_companies,
                )
            )
        return list_companies

    def update_user(self, id: int, data: UserIn, current_user: User) -> UserOut:
        user = self.user_repository.find_by_id(id)
        user.usr_nm = data.name
        user.usr_login = data.username
        user.usr_email = data.email
        user.id_company = data.company
        user.profile_id = data.profile
        return self.user_repository.update_user(user)
