from pydantic import BaseModel, Field, ConfigDict
from typing import List
from pydantic import RootModel

from tools.fakers import fake


class RegisterData(BaseModel):
    id: int
    login: str
    password: str = Field(alias="pass")
    games: list[str]


class Info(BaseModel):
    status: str
    message: str


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    register_data: RegisterData
    info: Info


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    login: str = Field(default_factory=fake.email)
    password: str = Field(alias="pass", default_factory=fake.password)


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    register_data: RegisterData
    info: Info

class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа получения пользователя.
    """
    id: int
    login: str
    password: str = Field(alias="pass")
    games: list[str]

class GetUsersResponseSchema(RootModel):
    """
    Описание структуры ответа получения пользователей.
    """
    root: List[str]
